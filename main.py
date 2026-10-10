#!/usr/bin/env python3
"""Inventário básico de arquivos e cálculo de SHA-256 para fins educacionais."""

import argparse
import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path


FIELDS = [
    "arquivo",
    "caminho_relativo",
    "extensao",
    "tamanho_bytes",
    "modificado_utc",
    "sha256",
    "status",
]


def sha256_file(path: Path) -> str:
    """Calcula o SHA-256 lendo o arquivo em blocos."""
    digest = hashlib.sha256()
    with path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(source: Path) -> list[dict[str, str | int]]:
    """Retorna registros dos arquivos encontrados, incluindo subpastas."""
    records = []
    for path in sorted(p for p in source.rglob("*") if p.is_file()):
        try:
            stat = path.stat()
            modified = datetime.fromtimestamp(
                stat.st_mtime, tz=timezone.utc
            ).isoformat(timespec="seconds")
            digest = sha256_file(path)
            status = "OK"
            size = stat.st_size
        except OSError as exc:
            modified = ""
            digest = ""
            status = f"ERRO: {exc.__class__.__name__}"
            try:
                size = path.stat().st_size
            except OSError:
                size = ""
        records.append({
            "arquivo": path.name,
            "caminho_relativo": str(path.relative_to(source)),
            "extensao": path.suffix.lower(),
            "tamanho_bytes": size,
            "modificado_utc": modified,
            "sha256": digest,
            "status": status,
        })
    return records


def write_csv(records: list[dict], output: Path) -> None:
    """Grava os registros em CSV UTF-8."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inventaria arquivos e calcula hashes SHA-256."
    )
    parser.add_argument("--source", type=Path, default=Path("amostras"),
                        help="Pasta com arquivos de teste autorizados.")
    parser.add_argument("--output", type=Path,
                        default=Path("relatorios/inventario.csv"),
                        help="Caminho do relatório CSV.")
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()

    if not source.exists() or not source.is_dir():
        parser.error(f"A pasta de origem não existe ou não é uma pasta: {source}")
    if output == source or source in output.parents:
        parser.error("O relatório não pode ser gravado dentro da pasta de amostras.")

    records = inventory(source)
    write_csv(records, output)
    successful = sum(1 for row in records if row["status"] == "OK")
    errors = len(records) - successful

    print(f"Arquivos encontrados: {len(records)}")
    print(f"Processados com sucesso: {successful}")
    print(f"Com erro: {errors}")
    print(f"Relatório: {output}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
