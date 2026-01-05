from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
ENTITY_DB = {
    "man": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["adult", "male"]
    },
    "woman": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["adult", "female"]
    },
    "person": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["generic"]
    },
    "child": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["young", "short"]
    },
    "robot": {
        "type": "robot",
        "skeleton": "mechanical_biped",
        "draw_fn": "drawRobot",
        "attributes": ["metallic"]
    },
    "dog": {
        "type": "animal",
        "skeleton": "quadruped",
        "draw_fn": "drawDog",
        "attributes": ["pet"]
    }
}
entity_documents = []
for entity, data in ENTITY_DB.items():
    description = (
        f"{entity} is a {data['type']} entity with a "
        f"{data['skeleton']} skeleton. "
        f"Attributes include {', '.join(data['attributes'])}."
    )
    entity_documents.append(
        Document(
            page_content=description,
            metadata={
                "entity": entity,
                "type": data["type"],
                "skeleton": data["skeleton"],
                "draw_fn": data["draw_fn"],
                "attributes": data["attributes"]
            }
        )
    )
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

faiss_db = FAISS.from_documents(entity_documents, embeddings)
faiss_db.save_local("faiss_indexes/entities")
