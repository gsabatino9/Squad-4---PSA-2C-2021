# Squad 4 - PSA 2C 2021
Squad 4 para el Trabajo práctico Grupal perteneciente a la materia Análisis de la Información I, FIUBA

## Run

```bash
pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload --host 0.0.0.0
```

## Migrations

### Create

`alembic revision -m "${migration name}"`

It gonna generate a new file into `migration/versions`. This files gonna have two functions `upgrade` and `downgrade`

For example, if you wanna add dome columns to table `tickets`

```python3
def upgrade:
    op.add_column(
        "ticket",
        sa.Column('otra_columna', sa.String)
    )

def downgrade:
    op.drop_column("ticket", "otra_columna")
```

### Run Migration

`alembic upgrade head`

### Downgrade Migration

`alembic downgrade -${N}`

Is how many migration you want to make it back. If you wanna make it back the last one just run

`alembic downgrade -1`

