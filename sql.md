# Bases de dato estructuradas(SQL)

## Comandos de postgresql

### Conectarte a psql

```bash
sudo -u postgres psql # Para conectarte con el usuario postgres

sudo -U <usuario> -d psql # Para conectarte con el usuario <usuario> a la base de datos psql
```

### Listar las bases de dato

```bash
\l
```

### Crear una base de datos

```bash
CREATE DATABASE <nombre de la base de datos>;
```

### Conectarse a la base de datos

```bash
\c <nombre de la base de datos>;
```

### Listar las tablas de la base de datos

```bash
\dt
```

### Crear una tabla

```sql
CREATE TABLE <nombre de la tabla> (
    <nombre del campo> <tipo de dato> <restricciones>,
    <nombre del campo> <tipo de dato> <restricciones>,
    <nombre del campo> <tipo de dato> <restricciones>,
);
```

### Insertar datos en una tabla

```sql
INSERT INTO <nombre de la tabla> (<nombre del campo>, <nombre del campo>, <nombre del campo>) VALUES (<valor del campo>, <valor del campo>, <valor del campo>);
```

### Listar los datos de una tabla

```sql
SELECT * FROM <nombre de la tabla>;
```

### Listar los datos de una tabla con un filtro

```sql
SELECT * FROM <nombre de la tabla>
WHERE <nombre del campo> = <valor del campo>;
```

### Listar los datos de una tabla con un filtro y un orden

```sql
SELECT * FROM <nombre de la tabla>
WHERE <nombre del campo> = <valor del campo>
ORDER BY <nombre del campo> ASC;
```

### Listar los datos de una tabla con un filtro y un orden y un limite

```sql
SELECT * FROM <nombre de la tabla>
WHERE <nombre del campo> = <valor del campo>
ORDER BY <nombre del campo> ASC
LIMIT <numero de datos>;
```

### Editar un dato de una tabla

```sql
UPDATE <nombre de la tabla> SET <nombre del campo> = <valor del campo> WHERE <nombre del campo> = <valor del campo>;
```

### Eliminar un dato de una tabla

```sql
DELETE FROM <nombre de la tabla> WHERE <nombre del campo> = <valor del campo>;
```

### Eliminar una tabla

```sql

DROP TABLE <nombre de la tabla>;
```

### Eliminar una base de datos

```sql
DROP DATABASE <nombre de la base de datos>;
```
