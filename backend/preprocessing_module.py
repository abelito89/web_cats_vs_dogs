# preprocessing_module.py

import numpy as np
import tensorflow as tf
from typing import Tuple

# Definimos los formatos de imagen permitidos
ALLOWLIST_FORMATS = (".bmp", ".gif", ".jpeg", ".jpg", ".png")

def preprocess_image_manually(
    image_path: str,
    image_size: Tuple[int, int] = (256, 256),
    color_mode: str = "rgb",
    interpolation: str = "bilinear",
    crop_to_aspect_ratio: bool = False,
    pad_to_aspect_ratio: bool = False,
) -> tf.Tensor:
    """
    Preprocesses a manually loaded image to match transformations typically applied by
    `tf.keras.utils.image_dataset_from_directory`.

    Parameters:
    -----------
    image_path : str
        The path to the image file.
    image_size : Tuple[int, int], optional
        The target size for resizing the image in (width, height) format. Defaults to (256, 256).
    color_mode : str, optional
        The desired color mode. Options are "rgb", "rgba", or "grayscale". Defaults to "rgb".
    interpolation : str, optional
        The interpolation method for resizing. Options include "bilinear", "nearest", etc.
        Defaults to "bilinear".
    crop_to_aspect_ratio : bool, optional
        If True, crops the image to maintain the aspect ratio during resizing.
        Defaults to False.
    pad_to_aspect_ratio : bool, optional
        If True, pads the image to maintain the aspect ratio during resizing.
        Cannot be used simultaneously with `crop_to_aspect_ratio`. Defaults to False.

    Returns:
    --------
    tf.Tensor
        A 4D tensor of shape (1, image_size[0], image_size[1], channels) containing the processed image.

    Raises:
    -------
    ValueError
        If `image_path` is in an unsupported format, or if `color_mode` is not one of the accepted values,
        or if both `pad_to_aspect_ratio` and `crop_to_aspect_ratio` are set to True.
    """
    
    # Verificar el formato de la imagen
    if not image_path.lower().endswith(ALLOWLIST_FORMATS):
        raise ValueError(f"Formato de imagen no soportado. Formatos permitidos: {ALLOWLIST_FORMATS}")

    # Determinar número de canales
    if color_mode == "rgb":
        num_channels = 3
    elif color_mode == "rgba":
        num_channels = 4
    elif color_mode == "grayscale":
        num_channels = 1
    else:
        raise ValueError(f"color_mode debe ser 'rgb', 'rgba', o 'grayscale'. Recibido: {color_mode}")
    
    # Cargar y decodificar la imagen
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=num_channels, expand_animations=False)
    
    # Validar que no se usen ambas opciones de aspecto al mismo tiempo
    if pad_to_aspect_ratio and crop_to_aspect_ratio:
        raise ValueError("Solo uno de `pad_to_aspect_ratio` o `crop_to_aspect_ratio` puede estar activado.")

    # Redimensionar y ajustar el aspecto según las opciones dadas
    if crop_to_aspect_ratio:
        img = tf.image.resize(img, image_size, method=interpolation)
    elif pad_to_aspect_ratio:
        img = tf.image.resize_with_pad(img, image_size[0], image_size[1], method=interpolation)
    else:
        img = tf.image.resize(img, image_size, method=interpolation)
    
    # Asegurar que el tamaño de la imagen es consistente
    img.set_shape((image_size[0], image_size[1], num_channels))

    # Añadir dimensión de batch para compatibilidad con modelos
    img = tf.expand_dims(img, axis=0)

    return img
