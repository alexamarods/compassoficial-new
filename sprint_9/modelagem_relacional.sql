-- -----------------------------------------------------
-- Schema concessionaria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema concessionaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `concessionaria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
USE `concessionaria` ;

-- -----------------------------------------------------
-- Table `concessionaria`.`pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`pais` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pais` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`estado` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `idPais` INT UNSIGNED NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_estado_pais1_idx` (`idPais` ASC) VISIBLE,
  CONSTRAINT `fk_estado_pais1`
    FOREIGN KEY (`idPais`)
    REFERENCES `concessionaria`.`pais` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`cidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`cidade` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `idEstado` INT UNSIGNED NOT NULL,
  `cidade` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cidade_estado1_idx` (`idEstado` ASC) VISIBLE,
  CONSTRAINT `fk_cidade_estado1`
    FOREIGN KEY (`idEstado`)
    REFERENCES `concessionaria`.`estado` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`cliente` (
  `idCliente` INT UNSIGNED NULL AUTO_INCREMENT,
  `idCidade` INT UNSIGNED NOT NULL,
  `nome` VARCHAR(60) NOT NULL,
  `sobrenome` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`idCliente`),
  INDEX `fk_cliente_cidade1_idx` (`idCidade` ASC) VISIBLE,
  CONSTRAINT `fk_cliente_cidade1`
    FOREIGN KEY (`idCidade`)
    REFERENCES `concessionaria`.`cidade` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `concessionaria`.`combustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`combustivel` (
  `id` INT UNSIGNED NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `concessionaria`.`vendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`vendedor` (
  `idVendedor` INT UNSIGNED NULL AUTO_INCREMENT,
  `nome` VARCHAR(90) NOT NULL,
  `sobrenome` VARCHAR(45) NOT NULL,
  `sexo` SMALLINT NOT NULL,
  PRIMARY KEY (`idVendedor`));


-- -----------------------------------------------------
-- Table `concessionaria`.`marca_carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`marca_carro` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `marca` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`modelo_carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`modelo_carro` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `idMarcaCarro` INT UNSIGNED NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_modelo_carro_marca_carro1_idx` (`idMarcaCarro` ASC) VISIBLE,
  CONSTRAINT `fk_modelo_carro_marca_carro1`
    FOREIGN KEY (`idMarcaCarro`)
    REFERENCES `concessionaria`.`marca_carro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`carro` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `idModeloCarro` INT UNSIGNED NOT NULL,
  `km` INT NOT NULL,
  `chassi` VARCHAR(90) NOT NULL,
  `ano` INT NOT NULL,
  `combustivel_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_carro_modelo_carro1_idx` (`idModeloCarro` ASC) VISIBLE,
  INDEX `fk_carro_combustivel1_idx` (`combustivel_id` ASC) VISIBLE,
  CONSTRAINT `fk_carro_modelo_carro1`
    FOREIGN KEY (`idModeloCarro`)
    REFERENCES `concessionaria`.`modelo_carro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carro_combustivel1`
    FOREIGN KEY (`combustivel_id`)
    REFERENCES `concessionaria`.`combustivel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `concessionaria`.`locacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`locacao` (
  `idLocacao` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idCarro` INT NOT NULL,
  `idVendedor` INT NOT NULL,
  `dataLocacao` DATE NOT NULL,
  `horaLocacao` TIME NOT NULL,
  `qtdDiaria` INT NOT NULL,
  `vlrDiaria` DECIMAL(8,2) NOT NULL,
  `dataEntrega` DATE NULL,
  `horaEntrega` TIME NULL,
  PRIMARY KEY (`idLocacao`),
  INDEX (`idCliente` ASC) VISIBLE,
  INDEX (`idCarro` ASC) VISIBLE,
  INDEX (`idVendedor` ASC) VISIBLE,
  CONSTRAINT ``
    FOREIGN KEY (`idCliente`)
    REFERENCES `concessionaria`.`cliente` (`idCliente`),
  CONSTRAINT ``
    FOREIGN KEY (`idCarro`)
    REFERENCES `concessionaria`.`carro` (`id`),
  CONSTRAINT ``
    FOREIGN KEY (`idVendedor`)
    REFERENCES `concessionaria`.`vendedor` (`idVendedor`));
