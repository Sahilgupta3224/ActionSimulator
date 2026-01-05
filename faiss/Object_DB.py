from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
OBJECT_DB = {
    "ball": {
        "shape": "circle",
        "draw_fn": "drawBall",
        "physics": "bounce"
    },
    "bottle": {
        "shape": "cylinder",
        "draw_fn": "drawBottle",
        "physics": "rigid"
    },
    "chair": {
        "shape": "rectangular",
        "draw_fn": "drawChair",
        "physics": "static"
    },
    "box": {
        "shape": "cube",
        "draw_fn": "drawBox",
        "physics": "rigid"
    },
    "book": {
        "shape": "flat_rect",
        "draw_fn": "drawBook",
        "physics": "flexible"
    },
    "cup": {
        "shape": "cylinder",
        "draw_fn": "drawCup",
        "physics": "liquid_container"
    }
}
object_documents = []

for obj, data in OBJECT_DB.items():
    description = (
        f"{obj} is an object with {data['shape']} shape, "
        f"physical behavior '{data['physics']}'."
    )

    object_documents.append(
        Document(
            page_content=description,
            metadata={
                "object": obj,
                "shape": data["shape"],
                "draw_fn": data["draw_fn"],
                "physics": data["physics"]
            }
        )
    )
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
object_faiss = FAISS.from_documents(object_documents, embeddings)
object_faiss.save_local("faiss_indexes/objects")
