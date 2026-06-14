from src.database import supabase
from datetime import date

FILE = "data.json"





def add_habit(name):
    if not name:
        raise ValueError("Nome inválido")

    supabase.table("habitos").insert({
        "nome": name,
        "descricao": str(date.today()),
        "concluido": False
    }).execute()


def list_habits():
    resultado = supabase.table("habitos").select("*").execute()
    return resultado.data

def complete_habit(index):
    habitos = supabase.table("habitos").select("*").execute().data

    if index < 0 or index >= len(habitos):
        raise IndexError("Índice inválido")

    habit_id = habitos[index]["id"]

    supabase.table("habitos").update({
        "concluido": True
    }).eq("id", habit_id).execute()
