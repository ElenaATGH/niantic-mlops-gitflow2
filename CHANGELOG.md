# Changelog
## [2.0.1] - 2026-10-19 (hotfix/v2.0.1)
- Modelo reentrenado con ventana ampliada: accuracy 93, precision 91, recall 90, F1 90 (la puerta de calidad bloqueó el primer intento, accuracy 88).
- Puerta de calidad con mínimos inclusivos (≥).
- Regla de disparo multiseñal: AVISO / REENTRENAR / HOTFIX. La alerta roja pasa de la semana 7 a la 6 y el reentrenamiento se prepara en la 5.

## [2.0.0] - 2026-10-05
- Churn v2.0 (accuracy 92 %; se degradó a 76 % en la semana 7), rating AAA-B, monitor de deriva (PSI), API /health y /drift/latest.
- Dockerfile y pipeline CI/CD con puerta de calidad.
