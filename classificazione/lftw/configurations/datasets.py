from cinnamon.configuration import Configuration, Param
from cinnamon.registry import register_class

from lftw.configurations.keys import NAMESPACE


@register_class(
    name="dataset",
    tags={"lftw"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWConfig(Configuration):
    directory: str = Param("/Users/federicadelduchetto/Desktop/HateSpeech/classificazione")
    target_category: str | None = Param(None)

@register_class(
    name="dataset",
    tags={"lftw", "test2"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWConfigTEST2(Configuration):
    directory: str = Param("/Users/federicadelduchetto/Desktop/HateSpeech/classificazione")
    target_category: str | None = Param(None)
    test_file: str = Param("test2.csv")


@register_class(
    name="dataset",
    tags={"lftw", "ethnicity"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWEthnicityConfig(LFTWConfig):
    target_category: str = Param("Ethnicity")

@register_class(
    name="dataset",
    tags={"lftw", "ethnicity", "test2"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWEthnicityConfig2(LFTWConfigTEST2):
    target_category: str = Param("Ethnicity")

@register_class(
    name="dataset",
    tags={"lftw", "gender"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWGenderConfig(LFTWConfig):
    target_category: str = Param("Gender")

@register_class(
    name="dataset",
    tags={"lftw", "gender", "test2"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWGenderConfig2(LFTWConfigTEST2):
    target_category: str = Param("Gender")

@register_class(
    name="dataset",
    tags={"lftw", "religion"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWReligionConfig(LFTWConfig):
    target_category: str = Param("Religion")

@register_class(
    name="dataset",
    tags={"lftw", "religion", "test2"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWReligionConfig2(LFTWConfigTEST2):
    target_category: str = Param("Religion")

@register_class(
    name="dataset",
    tags={"lftw", "sexual_orientation"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWSexOrConfig(LFTWConfig):
    target_category: str = Param("Sexual Orientation")

@register_class(
    name="dataset",
    tags={"lftw", "sexual_orientation", "test2"},
    namespace=NAMESPACE,
    component="lftw.components.loaders.LFTWLoader"
)
class LFTWSexOrConfig2(LFTWConfigTEST2):
    target_category: str = Param("Sexual Orientation")
