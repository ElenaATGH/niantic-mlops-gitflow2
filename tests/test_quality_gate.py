from niantic_mlops.quality_gate import evaluate


def test_modelo_v2_pasa_la_puerta():
    assert evaluate({"accuracy": 93, "precision": 91, "recall": 90, "f1_score": 90}) == []
    assert evaluate({"accuracy": 90, "precision": 85, "recall": 85, "f1_score": 88}) == []  # mínimos inclusivos


def test_modelo_en_crisis_semana_7_se_bloquea():
    fallos = evaluate({"accuracy": 76, "precision": 74, "recall": 71, "f1_score": 72})
    assert len(fallos) == 4


def test_accuracy_89_se_bloquea():
    assert evaluate({"accuracy": 89, "precision": 91, "recall": 90, "f1_score": 90})


def test_metricas_de_la_semana_7_del_repositorio_bloquean_el_despliegue():
    import json
    from pathlib import Path

    datos = Path(__file__).resolve().parent.parent / "data" / "metrics_semana7.json"
    assert len(evaluate(json.loads(datos.read_text(encoding="utf-8")))) == 4
