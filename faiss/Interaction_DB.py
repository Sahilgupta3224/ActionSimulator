from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
INTERACTION_DB = {
    "none": {"requires_object": False},
    "apply_force": {"requires_object": True},
    "embrace": {"requires_entity": True},
    "launch_object": {"requires_object": True},
    "receive_object": {"requires_object": True},
    "consume": {"requires_object": True},
    "carry": {"requires_object": True},
    "play_with": {"requires_object": True},
    "operate_machine": {"requires_object": True},
    "talk": {"requires_entity": False},
    "look_at": {"requires_target": True},
    "change_state": {"requires_object": True}
}
interaction_documents = []

for interaction, data in INTERACTION_DB.items():
    description = (
        f"{interaction} is an interaction type. "
        f"It requires an object: {data.get('requires_object', False)}. "
        f"It requires an entity: {data.get('requires_entity', False)}. "
        f"It requires a target: {data.get('requires_target', False)}."
    )

    interaction_documents.append(
        Document(
            page_content=description,
            metadata={
                "interaction": interaction,
                **data
            }
        )
    )

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

interaction_faiss = FAISS.from_documents(interaction_documents, embeddings)
interaction_faiss.save_local("faiss_indexes/interactions")