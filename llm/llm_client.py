from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from config import TOML_CONFIG

deepseek_chat_model: BaseChatModel = init_chat_model(
    model_provider=TOML_CONFIG.llm_config.provider,
    model=TOML_CONFIG.llm_config.model,
    base_url=TOML_CONFIG.llm_config.base_url,
    api_key=TOML_CONFIG.llm_config.api_key,
)
