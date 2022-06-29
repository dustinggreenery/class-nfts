import React, { useState } from "react"
import { Button, Input } from "@material-ui/core"

export const CreateNFT = () => {
    const [address, setAddress] = useState<string>("test")
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const newAddress = event.target.value === "" ? "" : String(event.target.value)
        setAddress(newAddress)
        console.log(newAddress)
    }

    return (
        <>
            <Button color="primary" size="large" variant="contained">
                Create NFT
            </Button>
            <Input onChange={handleInputChange} />
        </>
    )
}