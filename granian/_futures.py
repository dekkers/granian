def future_watcher_wrapper(inner):
    async def future_watcher(watcher):
        try:
            await inner(watcher.scope, watcher.proto)
        except Exception:
            watcher.err()
            raise
        watcher.done()

    return future_watcher
