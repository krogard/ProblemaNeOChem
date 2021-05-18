from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
PAY_TOKEN = env.str("PAY_TOKEN")
ADMIN = env.list("ADMIN")
IP = env.str("ip")

DB_User = env.str("DB_User")
DB_Pass = env.str("DB_Pass")
DB_Name = env.str("DB_Name")
DB_Host = env.str("DB_Host")

POSTGRESURI = f"postgresql://{DB_User}:{DB_Pass}@{IP}/{DB_Name}"
