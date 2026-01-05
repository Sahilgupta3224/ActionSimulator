from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
MOVEMENT_DB = {
    "move": {"speed": "normal", "axis": "horizontal"},
    "fast_move": {"speed": "fast", "axis": "horizontal"},
    "low_move": {"speed": "slow", "axis": "ground"},
    "sudden_move": {"speed": "burst", "axis": "any"},
    "vertical_move": {"speed": "normal", "axis": "vertical"},
    "aerial": {"speed": "normal", "axis": "air"},
    "aquatic": {"speed": "fluid", "axis": "water"},
    "stationary": {"speed": "none", "axis": "none"},
    "guided_move": {"speed": "controlled", "axis": "path"}
}
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
movement_documents = []

for movement, data in MOVEMENT_DB.items():
    description = (
        f"{movement} movement has {data['speed']} speed "
        f"along the {data['axis']} axis."
    )

    movement_documents.append(
        Document(
            page_content=description,
            metadata={
                "movement": movement,
                "speed": data["speed"],
                "axis": data["axis"]
            }
        )
    )

movement_faiss = FAISS.from_documents(movement_documents, embeddings)
movement_faiss.save_local("faiss_indexes/movements")
