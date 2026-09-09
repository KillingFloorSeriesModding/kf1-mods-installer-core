from tempo_binary_tool_manager import manager

from kf1_mods_installer_core import logger, settings, constants


tools_cache = manager.ToolsCache(
    main_tool_author=constants.APP_AUTHOR,
    main_tool_name=constants.APP_TITLE,
    logging_function=logger.log_message,
    cache_path=settings.cache_dir
)
