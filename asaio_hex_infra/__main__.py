import sys
from src.adapters.aws import AWSSession

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m hex-infra <command>")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "run":
        print("Running the hex-infra module...")
        aws_session = AWSSession()
        print(f"Created AWS session with region: {aws_session.session.region_name!r}")
        aws_client = aws_session.get_client('s3')
        try:
            aws_client.list_buckets()  # Example operation to ensure the client works
        except Exception as e:
            print(f"Error using AWS client: {e}")
        if sys.argv[2:]:
            print(f"Additional arguments: {sys.argv[2:]}")
            sum_args = sum(int(arg) for arg in sys.argv[2:] if arg.isdigit())
            equation = '+'.join([arg for arg in sys.argv[2:] if arg.isdigit()])
            print(f"This is the sum of all numeric args: {equation} = {sum_args!r}")
        # Add your run logic here
    elif command == "test":
        print("Running tests...")
        # Add your test logic here
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()