from datetime import datetime, timezone


PIPELINE_NAME = "product_ingestion"


def get_pipeline_state(connection):

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                pipeline_name,
                last_successful_run,
                last_processed_id,
                status
            FROM pipeline_state
            WHERE pipeline_name = %s
            """,
            (PIPELINE_NAME,)
        )

        return cursor.fetchone()


def update_pipeline_state(
    connection,
    last_processed_id=None,
    status="FAILED"
):

    now = datetime.now(timezone.utc)

    with connection.cursor() as cursor:

        if status == "SUCCESS":

            cursor.execute(
                """
                INSERT INTO pipeline_state (
                    pipeline_name,
                    last_successful_run,
                    last_processed_id,
                    status
                )
                VALUES (%s, %s, %s, %s)

                ON CONFLICT (pipeline_name)
                DO UPDATE SET
                    last_successful_run = EXCLUDED.last_successful_run,
                    last_processed_id = EXCLUDED.last_processed_id,
                    status = EXCLUDED.status
                """,
                (
                    PIPELINE_NAME,
                    now,
                    last_processed_id,
                    status
                )
            )

        else:

            cursor.execute(
                """
                INSERT INTO pipeline_state (
                    pipeline_name,
                    status
                )
                VALUES (%s, %s)

                ON CONFLICT (pipeline_name)
                DO UPDATE SET
                    status = EXCLUDED.status
                """,
                (
                    PIPELINE_NAME,
                    status
                )
            )