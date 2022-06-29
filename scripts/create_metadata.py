from venv import create
from scripts.helpful_scripts import get_student
from metadata.sample_metadata import metadata_template
from brownie import ClassNFT, network
from pathlib import Path
import requests
import json
import os

# Props to Lara to becoming the first nft. Noah is runner-up, and Nathan is third.
student_to_image_uri = {
    "AAKASH": "",
    "JONPAUL": "",
    "COHEN": "",
    "OAK": "",
    "JOHN": "",
    "EMELIO": "",
    "LUCAS": "https://ipfs.io/ipfs/QmYjAopFLEhJ43RFgePzo1Q53BBTXJ7jKCadRE8zpvUkXA?filename=lucas.png",
    "KARYSSA": "https://ipfs.io/ipfs/QmSv6EU95f7shtimNLUk2ZMGp7WahYQHuWjdfvZXb9XGoY?filename=karyssa.png",
    "NOAH": "https://ipfs.io/ipfs/QmcGkNThu941dpVf6vd9z2UDywNNZXqSSMNpen89VG4Cy9?filename=noah.png",
    "LARA": "https://ipfs.io/ipfs/QmQDmiSYzXVyhCcoC2U42bXyHTi7XMtp3V3EbrCoUBtYUP?filename=lara.png",
    "YAQING": "",
    "BELLE": "",
    "MATTEO": "",
    "JOHAN": "",
    "NATHAN": "https://ipfs.io/ipfs/QmWXQ8js1yZGUTWzyx44Xr1K5uWimgDiLxSTyJJyX9DLD8?filename=nathan.png",
    "KEVIN": "",
    "RYAN": "",
    "STEPHANIE": "",
    "DALUCHI": "",
    "ADAM": "",
    "AIDEN": "",
    "MATTHIAS": "",
    "MSKEDDY_SPECIAL": "https://ipfs.io/ipfs/QmXpYcGwNioFKwtRPQAGrGFRe5epKDx9uahYLNrEiWLKKK?filename=mskeddy_special.png",
}

student_to_attribute = {
    "AAKASH": "",
    "JONPAUL": "",
    "COHEN": "",
    "OAK": "",
    "JOHN": "",
    "EMELIO": "",
    "LUCAS": "",
    "KARYSSA": "",
    "NOAH": "noahtest",
    "LARA": "laratest",
    "YAQING": "",
    "BELLE": "",
    "MATTEO": "",
    "JOHAN": "",
    "NATHAN": "",
    "KEVIN": "",
    "RYAN": "",
    "STEPHANIE": "",
    "DALUCHI": "",
    "ADAM": "",
    "AIDEN": "",
    "MATTHIAS": "",
    "MSKEDDY_SPECIAL": "",
}


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        PINATA_BASE_URL = "https://api.pinata.cloud/"
        endpoint = "pinning/pinFileToIPFS"
        headers = {
            "pinata_api_key": os.getenv("PINATA_API_KEY"),
            "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
        }
        filename = filepath.split("/")[-1:][0]
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        ipfs_hash = response.json()["IpfsHash"]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri


def create_metadata():
    class_nft = ClassNFT[-1]
    number_of_class_nft = class_nft.tokenCounter()
    print(f"{number_of_class_nft} collectibles have been created.")
    for token_id in range(number_of_class_nft):
        student = get_student(class_nft.tokenIdToStudent(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{student}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists.")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = student
            collectible_metadata[
                "description"
            ] = f"{student} in the Grade 8 Gifted Program in St. Mark!"
            collectible_metadata["attributes"] = [
                {"trait_type": student_to_attribute[student], "value": 100}
            ]
            image_path = "./img/" + student.lower() + ".png"
            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else student_to_image_uri[student]

            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


def main():
    create_metadata()
