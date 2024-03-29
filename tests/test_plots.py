# stdlib
import importlib
from typing import Iterable, Tuple

# 3rd party
import pytest
from cawdrey import Tally
from matplotlib.figure import Figure  # type: ignore[import]
from matplotlib.text import Text  # type: ignore[import]

# this package
from domplotlib.plots import pie_from_tally
from tests.common import check_images


@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("style", ["default", "domdf"])
@check_images
def test_plot_pie_from_tally(reverse: bool, style: str):

	style_module = importlib.import_module(f"domplotlib.styles.{style}")
	importlib.reload(style_module)
	plt = style_module.plt

	data = [
			"cat",
			"dog",
			"dog",
			"cat",
			"rabbit",
			"dog",
			"dog",
			"cat",
			"snake",
			"gerbil",
			]

	tally = Tally(data)

	fig: Figure = plt.figure(figsize=(8, 8))
	ax = fig.subplots()

	patches, texts, autotexts = pie_from_tally(
		tally,
		[tally.most_common(1)[0][0]],
		autopct="%1.1f%%",
		startangle=90,
		ax=ax,
		reverse=reverse,
		)

	assert len(patches) == 5
	assert len(texts) == 5
	assert len(autotexts) == 5

	if reverse:
		most_common: Iterable[Tuple[str, int]] = reversed(tally.most_common())
	else:
		most_common = tally.most_common()

	text: Text
	for text, autotext, pet in zip(texts, autotexts, most_common):
		assert text.get_text() == pet[0]
		assert autotext.get_text() == f"{tally.get_percentage(pet[0]):0.1%}"

	ax.axis("equal", emit=True)

	return fig


@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("style", ["default", "domdf"])
@check_images
def test_plot_pie_from_tally_no_explode(reverse: bool, style: str):

	style_module = importlib.import_module(f"domplotlib.styles.{style}")
	importlib.reload(style_module)
	plt = style_module.plt

	data = [
			"cat",
			"dog",
			"dog",
			"cat",
			"rabbit",
			"dog",
			"dog",
			"cat",
			"snake",
			"gerbil",
			]

	tally = Tally(data)

	fig: Figure = plt.figure(figsize=(8, 8))
	ax = fig.subplots()

	patches, texts, autotexts = pie_from_tally(
		tally,
		autopct="%1.1f%%",
		startangle=90,
		ax=ax,
		reverse=reverse,
		)

	assert len(patches) == 5
	assert len(texts) == 5
	assert len(autotexts) == 5

	if reverse:
		most_common: Iterable[Tuple[str, int]] = reversed(tally.most_common())
	else:
		most_common = tally.most_common()

	text: Text
	for text, autotext, pet in zip(texts, autotexts, most_common):
		assert text.get_text() == pet[0]
		assert autotext.get_text() == f"{tally.get_percentage(pet[0]):0.1%}"

	ax.axis("equal", emit=True)

	return fig
