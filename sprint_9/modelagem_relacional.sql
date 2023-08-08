-- Criação das tabelas normalizadas

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

-- Inserção de dados nas tabelas normalizadas

-- Inserção em tb_cliente
INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) 
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente FROM tb_locacao;

-- Inserção em tb_combustivel
INSERT INTO tb_combustivel (idcombustivel, tipoCombustivel) 
SELECT DISTINCT idcombustivel, tipoCombustivel FROM tb_locacao;

-- Inserção em tb_vendedor
INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) 
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor FROM tb_locacao;

-- Inserção em tb_carro
INSERT INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel) 
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel FROM tb_locacao;

-- Inserção em tb_locacao_normalized
INSERT INTO tb_locacao_normalized (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) 
SELECT idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor FROM tb_locacao;
