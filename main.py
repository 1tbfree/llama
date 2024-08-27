import ollama
import subprocess

# Start a chat stream with the model 'tinyllama'
stream = ollama.chat(
    model='tinyllama',
    messages=[{'role': 'user', 'content': 'type random commands in chat'}],
    stream=True,
)

# Iterate through the stream and execute each command
for chunk in stream:
    command = chunk['message']['content'].strip()
    
    if command:  # Check if the command is not empty
        try:
            # Execute the command on the host system
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            # Print the output of the command
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            # Print the error if the command fails
            print(f"Error executing command '{command}': {e.stderr}")
