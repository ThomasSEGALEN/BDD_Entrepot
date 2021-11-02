-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`jobs` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `salary` DECIMAL NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`category` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `jobs_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_category_jobs1_idx` (`jobs_id` ASC),
  CONSTRAINT `fk_category_jobs1`
    FOREIGN KEY (`jobs_id`)
    REFERENCES `mydb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`products` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  `price` DECIMAL NOT NULL,
  `quantity` INT NOT NULL DEFAULT 0,
  `weight` FLOAT NOT NULL,
  `height` FLOAT NOT NULL,
  `category_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_products_category1_idx` (`category_id` ASC),
  CONSTRAINT `fk_products_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `mydb`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`slots`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`slots` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `disponible` VARCHAR(255) BINARY NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`warehouses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`warehouses` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `quantity_product_max` INT NOT NULL,
  `slots_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_warehouses_slots1_idx` (`slots_id` ASC),
  CONSTRAINT `fk_warehouses_slots1`
    FOREIGN KEY (`slots_id`)
    REFERENCES `mydb`.`slots` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`civility`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`civility` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`employees` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `lastname` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NOT NULL,
  `age` TINYINT NOT NULL,
  `jobs_id` BIGINT NOT NULL,
  `civility_id` BIGINT NOT NULL,
  `warehouse_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_employee_post_idx` (`post_id` ASC),
  INDEX `fk_employee_civility1_idx` (`civility_id` ASC),
  INDEX `fk_employee_warehouse1_idx` (`warehouse_id` ASC),
  CONSTRAINT `fk_employee_post`
    FOREIGN KEY (`post_id`)
    REFERENCES `mydb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_civility1`
    FOREIGN KEY (`civility_id`)
    REFERENCES `mydb`.`civility` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_warehouse1`
    FOREIGN KEY (`warehouse_id`)
    REFERENCES `mydb`.`warehouses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`warehouses_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`warehouses_has_products` (
  `products_id` BIGINT NOT NULL,
  `warehouse_id` BIGINT NOT NULL,
  PRIMARY KEY (`products_id`, `warehouse_id`),
  INDEX `fk_products_has_warehouse_warehouse1_idx` (`warehouse_id` ASC),
  INDEX `fk_products_has_warehouse_products1_idx` (`products_id` ASC),
  CONSTRAINT `fk_products_has_warehouse_products1`
    FOREIGN KEY (`products_id`)
    REFERENCES `mydb`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_warehouse_warehouse1`
    FOREIGN KEY (`warehouse_id`)
    REFERENCES `mydb`.`warehouses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`height`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`height` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `dimention` DECIMAL NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`products_has_slots`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`products_has_slots` (
  `products_id` BIGINT NOT NULL,
  `slots_id` BIGINT NOT NULL,
  PRIMARY KEY (`products_id`, `slots_id`),
  INDEX `fk_products_has_slots_slots1_idx` (`slots_id` ASC),
  INDEX `fk_products_has_slots_products1_idx` (`products_id` ASC),
  CONSTRAINT `fk_products_has_slots_products1`
    FOREIGN KEY (`products_id`)
    REFERENCES `mydb`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_slots_slots1`
    FOREIGN KEY (`slots_id`)
    REFERENCES `mydb`.`slots` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`lane`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`lane` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `slots_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_lane_slots1_idx` (`slots_id` ASC),
  CONSTRAINT `fk_lane_slots1`
    FOREIGN KEY (`slots_id`)
    REFERENCES `mydb`.`slots` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`level`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`level` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `number` INT NOT NULL,
  `lane_id` BIGINT NOT NULL,
  `height_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_level_lane1_idx` (`lane_id` ASC),
  INDEX `fk_level_height1_idx` (`height_id` ASC),
  CONSTRAINT `fk_level_lane1`
    FOREIGN KEY (`lane_id`)
    REFERENCES `mydb`.`lane` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_level_height1`
    FOREIGN KEY (`height_id`)
    REFERENCES `mydb`.`height` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
