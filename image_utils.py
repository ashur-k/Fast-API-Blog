import uuid
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

PROFILE_PICS_DIR = Path("media/profile_pics")


def process_profile_image(content: bytes) -> str:
    with Image.open(BytesIO(content)) as original:
        image = ImageOps.exif_transpose(original)
        image = ImageOps.fit(image, (300, 300), method=Image.Resampling.LANCZOS)

        if image.mode in ("RGBA", "LA", "P"):
            image = image.convert("RGB")

        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = PROFILE_PICS_DIR / filename
        PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True)
        image.save(filepath, "JPEG", quality=85, optimize=True)

    return filename


def delete_profile_image(filename: str) -> None:
    if filename is None:
        return
    
    file_path = PROFILE_PICS_DIR / filename
    if file_path.exists():
        file_path.unlink()