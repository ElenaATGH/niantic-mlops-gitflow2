"""Puerta de calidad del pipeline CI/CD: bloquea el despliegue si el modelo no cumple los mínimos."""
import json
import sys

# Mínimos (inclusivos: accuracy ≥ 90, precision ≥ 85, recall ≥ 85, F1 ≥ 88) definidos en la memoria, diapositiva "Pipeline CI/CD con puertas de calidad".
GATE = {"accuracy": 90, "precision": 85, "recall": 85, "f1_score": 88}


def evaluate(metrics: dict) -> list[str]:
    """Devuelve la lista de fallos; vacía si el modelo puede promocionarse."""
    return [
        f"{name} {metrics[name]} < {minimum}"
        for name, minimum in GATE.items()
        if metrics[name] < minimum
    ]


def main(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        metrics = json.load(fh)
    failures = evaluate(metrics)
    if failures:
        print("PUERTA DE CALIDAD: BLOQUEADO ->", "; ".join(failures))
        return 1
    print("PUERTA DE CALIDAD: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
