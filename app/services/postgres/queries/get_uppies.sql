-- get_uppies.sql
-- Selects urls to run before everything else, uppies
SELECT
    id AS url_id,
    url
FROM
    targets.urls
WHERE
    (worker_status ->> 'uppies')::BOOLEAN = TRUE
    AND (
        (worker_queued_at ->> 'uppies') IS NULL
        OR (worker_queued_at ->> 'uppies')::TIMESTAMP WITH TIME ZONE <= CURRENT_TIMESTAMP - INTERVAL '2 hours'
    )
ORDER BY
    (worker_history -> 'uppies' -> 'recent_run') IS NULL DESC,
    (worker_history -> 'uppies' ->> 'recent_run')::TIMESTAMP WITH TIME ZONE ASC
LIMIT 10;
