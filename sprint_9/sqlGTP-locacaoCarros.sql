-- Tabela tb_cliente
CREATE TABLE tb_cliente (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente TEXT,
    cidadeCliente TEXT,
    estadoCliente TEXT,
    paisCliente TEXT
);

-- Tabela tb_combustivel
CREATE TABLE tb_combustivel (
    idcombustivel INTEGER PRIMARY KEY,
    tipoCombustivel TEXT
);

-- Tabela tb_vendedor
CREATE TABLE tb_vendedor (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor TEXT,
    sexoVendedor INTEGER,
    estadoVendedor TEXT
);

-- Tabela tb_carro
CREATE TABLE tb_carro (
    idCarro INTEGER PRIMARY KEY,
    kmCarro INTEGER,
    classiCarro TEXT,
    marcaCarro TEXT,
    modeloCarro TEXT,
    anoCarro INTEGER,
    idcombustivel INTEGER,
    FOREIGN KEY (idcombustivel) REFERENCES tb_combustivel(idcombustivel)
);

-- Tabela tb_locacao_normalized
CREATE TABLE tb_locacao_normalized (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idCarro INTEGER,
    dataLocacao INTEGER,
    horaLocacao TEXT,
    qtdDiaria INTEGER,
    vlrDiaria INTEGER,
    dataEntrega INTEGER,
    horaEntrega TEXT,
    idVendedor INTEGER,
    FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);