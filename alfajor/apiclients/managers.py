from logging import getLogger

from alfajor.utilities import eval_dotted_path


__all__ = ['WSGIManager', 'ZeroManager']
logger = getLogger('alfajor')


class WSGIManager(object):
    """Lifecycle manager for global WSGI HTTP api clients."""

    def __init__(self, frontend_name, backend_config, runner_options):
        self.config = backend_config

    def create(self):
        from alfajor.apiclients.wsgi import WSGI

        entry_point = self.config['server-entry-point']
        app = eval_dotted_path(entry_point)

        base_url = self.config.get('base_url')
        logger.debug("Created in-process WSGI api client rooted at %s.",
                     base_url)
        return WSGI(app, base_url=base_url)

    def destroy(self):
        logger.debug("Destroying in-process WSGI api client.")


class ZeroManager(object):
    """Lifecycle manager for global Zero HTTP api clients."""

    def __init__(self, frontend_name, backend_config, runner_options):
        pass

    def create(self):
        from alfajor.apiclients.zero import Zero
        logger.debug("Creating Zero api client.")
        return Zero()

    def destroy(self):
        logger.debug("Destroying Zero api client.")
