-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema recettes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema recettes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recettes` DEFAULT CHARACTER SET latin1 ;
USE `recettes` ;

-- -----------------------------------------------------
-- Table `recettes`.`utilisateur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recettes`.`utilisateur` (
  `idUtilisateur` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_U` VARCHAR(45) NULL DEFAULT NULL,
  `prenom_U` VARCHAR(45) NULL DEFAULT NULL,
  `pseudo_U` VARCHAR(45) NULL DEFAULT NULL,
  `mdp_U` VARCHAR(45) NULL DEFAULT NULL,
  `admin_U` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idUtilisateur`))
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `recettes`.`recettes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recettes`.`recettes` (
  `id_R` INT(11) NOT NULL AUTO_INCREMENT,
  `Nom_R` VARCHAR(45) NULL DEFAULT NULL,
  `Description_R` VARCHAR(5000) NULL DEFAULT NULL,
  `Auteur_R` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_R`),
  INDEX `Auteur_R` (`Auteur_R` ASC) VISIBLE,
  CONSTRAINT `recettes_ibfk_1`
    FOREIGN KEY (`Auteur_R`)
    REFERENCES `recettes`.`utilisateur` (`idUtilisateur`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `recettes`.`commentaire`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recettes`.`commentaire` (
  `id_U` INT(11) NOT NULL,
  `id_R` INT(11) NOT NULL,
  `Commentaire` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_U`, `id_R`),
  INDEX `id_R` (`id_R` ASC) VISIBLE,
  CONSTRAINT `commentaire_ibfk_1`
    FOREIGN KEY (`id_U`)
    REFERENCES `recettes`.`utilisateur` (`idUtilisateur`)
    ON DELETE CASCADE,
  CONSTRAINT `commentaire_ibfk_2`
    FOREIGN KEY (`id_R`)
    REFERENCES `recettes`.`recettes` (`id_R`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `recettes`.`ingrédients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recettes`.`ingrédients` (
  `id_I` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_I` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_I`, `nom_I`))
ENGINE = InnoDB
AUTO_INCREMENT = 34
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `recettes`.`quantitéingrédients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recettes`.`quantitéingrédients` (
  `id_R` INT(11) NOT NULL,
  `id_I` INT(11) NOT NULL,
  `Quantité` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_R`, `id_I`),
  INDEX `id_I` (`id_I` ASC) VISIBLE,
  CONSTRAINT `quantitéingrédients_ibfk_1`
    FOREIGN KEY (`id_R`)
    REFERENCES `recettes`.`recettes` (`id_R`)
    ON DELETE CASCADE,
  CONSTRAINT `quantitéingrédients_ibfk_2`
    FOREIGN KEY (`id_I`)
    REFERENCES `recettes`.`ingrédients` (`id_I`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;







/*CREATE TABLE `ingrédients` (
  `id_I` int(11) NOT NULL AUTO_INCREMENT,
  `nom_I` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_I`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `utilisateur` (
  `idUtilisateur` int(11) NOT NULL AUTO_INCREMENT,
  `nom_U` varchar(45) DEFAULT NULL,
  `prenom_U` varchar(45) DEFAULT NULL,
  `pseudo_U` varchar(45) DEFAULT NULL,
  `mdp_U` varchar(45) DEFAULT NULL,
  `admin_U` int(11) DEFAULT NULL,
  PRIMARY KEY (`idUtilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `recettes` (
  `id_R` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_R` varchar(45) DEFAULT NULL,
  `Description_R` varchar(5000) DEFAULT NULL,
  `Auteur_R` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_R`),
  KEY `Auteur_R` (`Auteur_R`),
  CONSTRAINT `recettes_ibfk_1` FOREIGN KEY (`Auteur_R`) REFERENCES `utilisateur` (`idUtilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `commentaire` (
  `id_U` int(11) NOT NULL,
  `id_R` int(11) NOT NULL,
  `Commentaire` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_U`,`id_R`),
  KEY `id_R` (`id_R`),
  CONSTRAINT `commentaire_ibfk_1` FOREIGN KEY (`id_U`) REFERENCES `utilisateur` (`idUtilisateur`),
  CONSTRAINT `commentaire_ibfk_2` FOREIGN KEY (`id_R`) REFERENCES `recettes` (`id_R`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE `quantitéingrédients` (
  `id_R` int(11) NOT NULL,
  `id_I` int(11) NOT NULL,
  `Quantité` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_R`,`id_I`),
  KEY `id_I` (`id_I`),
  CONSTRAINT `quantitéingrédients_ibfk_1` FOREIGN KEY (`id_R`) REFERENCES `recettes` (`id_R`),
  CONSTRAINT `quantitéingrédients_ibfk_2` FOREIGN KEY (`id_I`) REFERENCES `ingrédients` (`id_I`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;*/



