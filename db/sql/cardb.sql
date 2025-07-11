USE cardb;

DROP TABLE IF EXISTS subsidy;
DROP TABLE IF EXISTS eco_car_info;
DROP TABLE IF EXISTS engine_car_info;
DROP TABLE IF EXISTS car_info;

-- 차량 정보
CREATE TABLE car_info (
    car_code INT AUTO_INCREMENT PRIMARY KEY,
    f_type VARCHAR(100) NOT NULL,
     UNIQUE KEY unique_type (f_type)
) ENGINE=InnoDB;

-- 친환경차 정보
CREATE TABLE eco_car_info (
    idex INT NOT NULL PRIMARY KEY,
    car_code INT NOT NULL,
    year INT NOT NULL,
    area VARCHAR(100) NOT NULL,
    total INT NOT NULL,
    CONSTRAINT fk_eco_car FOREIGN KEY (car_code) REFERENCES car_info(car_code)
) ENGINE=InnoDB;

-- 내연기관차 정보
CREATE TABLE engine_car_info (
    idex INT NOT NULL PRIMARY KEY,
    car_code INT NOT NULL,
    year INT NOT NULL,
    area VARCHAR(100) NOT NULL,
    total INT NOT NULL,
    CONSTRAINT fk_engine_car FOREIGN KEY (car_code) REFERENCES car_info(car_code)
) ENGINE=InnoDB;

-- 보조금 정보
CREATE TABLE subsidy (
    idex INT NOT NULL,
    car_code INT NOT NULL,
    year INT NOT NULL,
    area VARCHAR(100) NOT NULL,
    amount INT NOT NULL,
    PRIMARY KEY (idex),
    CONSTRAINT fk_subsidy_car FOREIGN KEY (car_code) REFERENCES car_info(car_code),
    CONSTRAINT fk_subsidy_eco FOREIGN KEY (idex) REFERENCES eco_car_info(idex)
) ENGINE=InnoDB;

select * from eco_car_info;
select * from engine_car_info;
select * from car_info;
select * from subsidy;