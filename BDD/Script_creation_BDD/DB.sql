-- MySQL Workbench Forward Engineering

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
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `salary` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`category` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `jobs_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_category_jobs1_idx` (`jobs_id` ASC),
  CONSTRAINT `fk_category_jobs1`
    FOREIGN KEY (`jobs_id`)
    REFERENCES `mydb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`civility`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`civility` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`warehouses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`warehouses` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `quantity_product_max` INT(11) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`employees` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `lastname` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NOT NULL,
  `age` TINYINT(4) NOT NULL,
  `jobs_id` BIGINT(20) NOT NULL,
  `civility_id` BIGINT(20) NOT NULL,
  `warehouse_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_employee_post_idx` (`jobs_id` ASC),
  INDEX `fk_employee_civility1_idx` (`civility_id` ASC),
  INDEX `fk_employee_warehouse1_idx` (`warehouse_id` ASC),
  CONSTRAINT `fk_employee_civility1`
    FOREIGN KEY (`civility_id`)
    REFERENCES `mydb`.`civility` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_post`
    FOREIGN KEY (`jobs_id`)
    REFERENCES `mydb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_warehouse1`
    FOREIGN KEY (`warehouse_id`)
    REFERENCES `mydb`.`warehouses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`height`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`height` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `dimension` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`slots`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`slots` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `disponible` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NULL DEFAULT NULL,
  `warehouses_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_slots_warehouses1_idx` (`warehouses_id` ASC),
  CONSTRAINT `fk_slots_warehouses1`
    FOREIGN KEY (`warehouses_id`)
    REFERENCES `mydb`.`warehouses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`lane`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`lane` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `slots_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_lane_slots1_idx` (`slots_id` ASC),
  CONSTRAINT `fk_lane_slots1`
    FOREIGN KEY (`slots_id`)
    REFERENCES `mydb`.`slots` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`level`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`level` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `number` INT(11) NOT NULL,
  `lane_id` BIGINT(20) NOT NULL,
  `height_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_level_lane1_idx` (`lane_id` ASC),
  INDEX `fk_level_height1_idx` (`height_id` ASC),
  CONSTRAINT `fk_level_height1`
    FOREIGN KEY (`height_id`)
    REFERENCES `mydb`.`height` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_level_lane1`
    FOREIGN KEY (`lane_id`)
    REFERENCES `mydb`.`lane` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`products` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `quantity` INT(11) NOT NULL DEFAULT '0',
  `weight` FLOAT NOT NULL,
  `height` FLOAT NOT NULL,
  `category_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_products_category1_idx` (`category_id` ASC),
  CONSTRAINT `fk_products_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `mydb`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`products_has_slots`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`products_has_slots` (
  `products_id` BIGINT(20) NOT NULL,
  `slots_id` BIGINT(20) NOT NULL,
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
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`warehouses_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`warehouses_has_products` (
  `products_id` BIGINT(20) NOT NULL,
  `warehouse_id` BIGINT(20) NOT NULL,
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
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;