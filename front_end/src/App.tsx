import React from 'react';
import { DAppProvider, ChainId } from '@usedapp/core';
import { Header } from "./components/Header"
import { Container } from "@material-ui/core"
import { Main } from "./components/Main"
import { CreateNFT } from "./components/CreateNFT"

function App() {
  return (
    <DAppProvider config={{
      supportedChains: [ChainId.Rinkeby]
    }}>
      <Header />
      <Container maxWidth="lg">
        <div>Hello World!</div>
        <Main />
        <CreateNFT />
      </Container>
    </DAppProvider>
  );
}

export default App;
