from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
LOCATION_DB = {
    "in the room": {"anchor": "room_center"},
    "on the table": {"anchor": "surface_top"},
    "near the door": {"anchor": "door_proximity"},
    "in the park": {"anchor": "outdoor_ground"},
    "beside the chair": {"anchor": "object_side"},
    "under the table": {"anchor": "under_surface"},
    "next to the shelf": {"anchor": "object_side"}
}
location_documents = []

for location, data in LOCATION_DB.items():
    description = (
        f"{location} describes a spatial location anchored at "
        f"{data['anchor']}."
    )

    location_documents.append(
        Document(
            page_content=description,
            metadata={
                "location": location,
                "anchor": data["anchor"]
            }
        )
    )
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
location_faiss = FAISS.from_documents(location_documents, embeddings)
location_faiss.save_local("faiss_indexes/locations")
