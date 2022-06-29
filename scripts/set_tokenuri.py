from brownie import network, ClassNFT, accounts
from scripts.helpful_scripts import OPENSEA_URL, get_student, get_account

student_metadata_dic = {
    "AAKASH": "",
    "JONPAUL": "",
    "COHEN": "",
    "OAK": "",
    "JOHN": "",
    "EMELIO": "",
    "LUCAS": "https://ipfs.io/ipfs/QmWjqnnyRwZBjaLsNZb3w9seDaBcUfHAGfoPHQNabq55ey?filename=0-LUCAS.json",
    "KARYSSA": "https://ipfs.io/ipfs/QmTCHFzr6BHj5k8Q216nYN3s7oghCNX3Ditb2U5kPCsp99?filename=0-KARYSSA.json",
    "NOAH": "https://ipfs.io/ipfs/QmTehgEr4pggqDk9wAGEczWPMhp7F2CBByL9KJ3dp9Xvvr?filename=1-NOAH.json",
    "LARA": "https://ipfs.io/ipfs/QmQYqH5PxkEffhD4YvKodJUDuKVFAYKS4P2nfRUKj8VVWb?filename=0-LARA.json",
    "YAQING": "",
    "BELLE": "",
    "MATTEO": "",
    "JOHAN": "",
    "NATHAN": "https://ipfs.io/ipfs/QmdH2U55xeuv4UU6KnuVmXKTT4pHXdME14JDMyUaRkrtd7?filename=2-NATHAN.json",
    "KEVIN": "",
    "RYAN": "",
    "STEPHANIE": "",
    "DALUCHI": "",
    "ADAM": "",
    "AIDEN": "",
    "MATTHIAS": "",
    "MSKEDDY_SPECIAL": "",
}


def set_tokenURI(token_id, nft_contract, tokenURI, buyer):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": get_account(buyer)})
    tx.wait(1)
    print(
        f"You can now view NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("May take up to 20 minutes, make sure to hit the refresh metadata button")


def set_token_uri(buyer):
    print(f"Working on {network.show_active()}")
    class_nft = ClassNFT[-1]
    number_of_collectibles = class_nft.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        student = get_student(class_nft.tokenIdToStudent(token_id))
        if not class_nft.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, class_nft, student_metadata_dic[student], buyer)


def main():
    set_token_uri("0x7ae7a29b784e2a9151860133d64b7f12baa052abfafc0f22c4be9ba051d74a2e")
