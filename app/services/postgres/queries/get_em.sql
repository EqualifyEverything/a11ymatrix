-- get_em.sql
-- Selects urls to run with everything but uppies
SELECT
    id AS url_id,
    url
FROM
    targets.urls
WHERE
    (worker_status ->> '%s')::BOOLEAN = TRUE
    AND (
        (worker_queued_at ->> '%s') IS NULL
        OR (worker_queued_at ->> '%s')::TIMESTAMP WITH TIME ZONE <= CURRENT_TIMESTAMP - INTERVAL '2 hours'
    )
    AND (summary ->> 'http_code') LIKE '2%'
ORDER BY
    (worker_history -> '%s' -> 'recent_run') IS NULL DESC,
    (worker_history -> '%s' ->> 'recent_run')::TIMESTAMP WITH TIME ZONE ASC
LIMIT 10;
