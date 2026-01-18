import os

from pydantic import BaseModel, Field


class LlmConfig(BaseModel):
    """大语言模型配置"""

    provider: str = Field(default="deepseek", description="提供者")

    model: str = Field(default="deepseek-chat", description="模型名")

    api_key: str = Field(default="", description="API KEY")

    base_url: str = Field(default="https://api.deepseek.com", description="URL 前缀")


class SearchConfig(BaseModel):
    """搜索配置"""

    provider: str = Field(default="tavily", description="提供者")

    api_key: str = Field(default="", description="API KEY")


class LangSmithConfig(BaseModel):
    """LangSmith 追踪配置"""

    tracing: bool = Field(default=False, description="是否启用追踪")

    api_key: str = Field(default="", description="API KEY")


class TomlConfig(BaseModel):
    """Toml 配置"""

    llm_config: LlmConfig = Field(default_factory=LlmConfig, description="大语言模型配置")

    search_config: SearchConfig = Field(default_factory=SearchConfig, description="搜索配置")

    langsmith_config: LangSmithConfig = Field(default_factory=LangSmithConfig, description="LangSmith 追踪配置")


def load_toml_config(file_path: str = ".config.toml") -> TomlConfig:
    """加载 .config.toml 的配置"""

    import tomllib
    from pathlib import Path

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError

    try:
        with open(str(path), "rb") as f:
            toml_data = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        raise e

    return TomlConfig(
        llm_config=LlmConfig(**toml_data.get("llm")),
        search_config=SearchConfig(**toml_data.get("search")),
        langsmith_config=LangSmithConfig(**toml_data.get("langsmith")),
    )


TOML_CONFIG = load_toml_config()

if TOML_CONFIG.langsmith_config.tracing:
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_API_KEY"] = TOML_CONFIG.langsmith_config.api_key
