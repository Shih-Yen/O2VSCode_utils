###################################
# This is a script to start a computi on a Slurm cluster and prints the hostname
###################################
# Slurm job parameters
PARTITION=priority
CPU_CORES=4
MEMORY=24G
TIME_HOURS=12
JOB_NAME="vscodetunnel"
##

# sbatch and get the jobID
job_id=$(sbatch -p $PARTITION -c $CPU_CORES --mem=$MEMORY -t $TIME_HOURS:00:00 --job-name="$JOB_NAME" --wrap="sleep ${TIME_HOURS}h" | grep "Submitted batch job" | cut -d" " -f 4)
# Loop until the job starts, or 5 minutes have passed
end_time=$(( $(date +%s) + 300 )) # 300 seconds = 5 minutes
while [[ $(date +%s) -lt $end_time ]]; do
  # Check the job status using squeue
  job_state=$(squeue -j "$job_id" -h -o "%T" 2>/dev/null)

  # If the job is in a running state (RUNNING or COMPLETING)
  if [[ "$job_state" == "RUNNING" || "$job_state" == "COMPLETING" ]]; then
    echo "Job $job_id has started. Connecting..."
    srun --jobid "$job_id" /bin/bash -l -c "hostname" # Connect to the job using srun
    break  # Exit the loop after connecting
  else
    echo "Job $job_id is not running yet. Current state: $job_state"
  fi
  sleep 10  # Wait for 10 seconds before checking again
done