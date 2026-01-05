from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
LAYOUT_DB = {
    "none": {"pose": "neutral"},
    "seated": {"pose": "sit"},
    "lying": {"pose": "horizontal"},
    "prone": {"pose": "face_down"},
    "airborne": {"pose": "floating"},
    "close_proximity": {"pose": "near_target"}
}
layout_documents = []

for layout, data in LAYOUT_DB.items():
    description = f"{layout} layout corresponds to a {data['pose']} pose."

    layout_documents.append(
        Document(
            page_content=description,
            metadata={
                "layout": layout,
                "pose": data["pose"]
            }
        )
    )
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
layout_faiss = FAISS.from_documents(layout_documents, embeddings)
layout_faiss.save_local("faiss_indexes/layouts")
