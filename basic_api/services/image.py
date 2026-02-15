from dotenv import load_dotenv
import os
from imagekitio import ImageKit

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)

# Store URL endpoint for reuse
URL_ENDPOINT = os.environ.get("IMAGEKIT_URL")
