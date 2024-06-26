import sys
import asyncio
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import print_banner,print_with_timestamp, main
from src.Battle import merah

if __name__ == "__main__":
    try:
        asyncio.run(main())
        print_banner()
    except KeyboardInterrupt:
        print_with_timestamp(f"{merah}Program terminated by user.")
        sys.exit()
