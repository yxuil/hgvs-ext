"""hgvs extended module
Extend the `hgvs` package with additional functionality.
- AssemblyMapper:
   * c_to_c, p_to_p (default genome version: GRCh37)
   * p_to_c, p_to_g (best guesses only. Use with caution)
- Validator:
   * _intronic_variant_validator
   * _interval_variant_validator
- cdot:
   * trancript_id to gene symbol
   * protein_id to gene symbol
"""
from pathlib import Path

import hgvs.dataproviders.uta
from cdot.hgvs.dataproviders.uta import JSONDataProvier
import hgvs.normalizer
from hgvs.assemblymapper import AssemblyMapper
from hgvs.validator import Validator
from hgvs.parser import Parser
from hgvs.sequencevariant import SequenceVariant
from hgvs.dataproviders.uta import UTA_postgresql
from hgvs.exceptions import HGVSDataNotAvailableError, HGVSInvalidVariantError, HGVSInvalidIntervalError

from hgvs_ext.settings import CDOT_JSON_DIR, GENOME_VERSION

hgvs.global_config.mapping.replace_reference = False
hgvs.global_config.validation.strict = True
hgvs.global_config.formatting.p_3_letter = False
hgvs.global_config.mapping.assembly = GENOME_VERSION
cdot_json = [str(i) for i in Path(CDOT_JSON_DIR).glob("*.json.gz")]


def uta_get_tx_ac_for_pro_ac(self, protein_id: str) -> list[str]:
    """Get transcript accession number(s) for protein accession number"""
    query = (
        "select * from associated_accessions where pro_ac = %s order by pro_ac desc\n"
    )
    rows = self._fetchall(query, (protein_id,))
    return [row["tx_ac"] for row in rows] if rows else None


UTA_postgresql.get_tx_ac_for_pro_ac = uta_get_tx_ac_for_pro_ac

def uta_get_gene_for_tx_ac(self, transcript_id: str) -> str:
    pass