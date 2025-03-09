from pydantic import BaseModel

class Variant(BaseModel):
    gene: str = None
    chromosome: int = None
    genome_version: str = None
    genomic_change: str = None
    transcript_id: str = None
    coding_change: str = None
    protein_id: str = None
    protein_change: str = None
    exon: int = None

