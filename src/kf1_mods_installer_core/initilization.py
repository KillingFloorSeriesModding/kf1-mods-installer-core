import os
import asyncio

from kf1_mods_installer_core.checks import online_check
from kf1_mods_installer_core.tools import kf_temp_archive_extractor, steamcmd
from kf1_mods_installer_core import logger, settings, manager


def initilization():
    online_check.init_is_online()
    print(f"Is online: {online_check.is_online}")
    logger.set_log_base_dir(os.path.normpath(f"{settings.script_dir}/logs"))
    logger.configure_logging()
    if online_check.is_online:
        asyncio.run(ensure_needed_tools_are_installed())
    else:
        raise RuntimeError(('You need to be online when using this tool, to download steamcmd, KFTempArchiveExtractor, and to download from the steam workshop.'))


async def ensure_needed_tools_are_installed():
    kf_temp_archive_extractor.KfTempArchiveExtractorToolInfo(cache=manager.tools_cache).ensure_tool_installed()
    steamcmd.SteamCmdToolInfo(cache=manager.tools_cache).ensure_tool_installed()
