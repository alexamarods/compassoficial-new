-- -----------------------------------------------------
-- Schema concessionaria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema concessionaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `concessionaria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
USE `concessionaria` ;

-- -----------------------------------------------------
-- Table `concessionaria`.`DimCliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`DimCliente` (
  `ClienteKey` INT UNSIGNED NULL DEFAULT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(120) NOT NULL,
  `Cidade` VARCHAR(90) NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  `Pais` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`ClienteKey`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`DimVendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`DimVendedor` (
  `VendedorKey` INT UNSIGNED NULL DEFAULT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(120) NOT NULL,
  `Sexo` SMALLINT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`VendedorKey`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`DimCarro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`DimCarro` (
  `CarroKey` INT UNSIGNED NULL DEFAULT NULL AUTO_INCREMENT,
  `Chassi` VARCHAR(20) NOT NULL,
  `Ano` INT NOT NULL,
  `Modelo` VARCHAR(45) NOT NULL,
  `Marca` VARCHAR(90) NOT NULL,
  `TipoCombustivel` VARCHAR(45) NOT NULL,
  `Km` INT NOT NULL,
  PRIMARY KEY (`CarroKey`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`DimTempo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`DimTempo` (
  `TempoKey` INT UNSIGNED NULL DEFAULT NULL AUTO_INCREMENT,
  `DataHoraLocacao` DATETIME NOT NULL,
  `DataHoraEntrega` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`TempoKey`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concessionaria`.`FatoLocacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concessionaria`.`FatoLocacao` (
  `LocacaoKey` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ClienteKey` INT UNSIGNED NOT NULL,
  `VendedorKey` INT UNSIGNED NOT NULL,
  `CarroKey` INT UNSIGNED NOT NULL,
  `TempoKey` INT UNSIGNED NOT NULL,
  `QtdDiaria` INT NOT NULL,
  `VlrDiaria` DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (`LocacaoKey`),
  INDEX (`ClienteKey` ASC) VISIBLE,
  INDEX (`VendedorKey` ASC) VISIBLE,
  INDEX (`CarroKey` ASC) VISIBLE,
  INDEX (`TempoKey` ASC) VISIBLE,
  CONSTRAINT ``
    FOREIGN KEY (`ClienteKey`)
    REFERENCES `concessionaria`.`DimCliente` (`ClienteKey`),
  CONSTRAINT ``
    FOREIGN KEY (`VendedorKey`)
    REFERENCES `concessionaria`.`DimVendedor` (`VendedorKey`),
  CONSTRAINT ``
    FOREIGN KEY (`CarroKey`)
    REFERENCES `concessionaria`.`DimCarro` (`CarroKey`),
  CONSTRAINT ``
    FOREIGN KEY (`TempoKey`)
    REFERENCES `concessionaria`.`DimTempo` (`TempoKey`))
ENGINE = InnoDB;