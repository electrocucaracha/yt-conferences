"""Regression checks for generated video players."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from style_site import PAGE_NAVIGATION, collection_navigation, embed_videos


class PageNavigationTests(unittest.TestCase):
    """Check collection order, boundaries, and safe link rendering."""

    def test_collection_navigation(self) -> None:
        with TemporaryDirectory() as directory:
            destination = Path(directory)
            collection = destination / "conference"
            collection.mkdir()
            (collection / "index.html").write_text(
                '<a href="outside.html">Outside article</a>'
                '<article class="kiso-content">'
                '<a href="b.html">B &amp; <em>first</em></a>'
                '<a href="a.html">A second</a>'
                '<a href="c.html">C third</a>'
                '<a href="b.html">Duplicate</a>'
                '<a href="index.html">Index</a>'
                '<a href="https://example.com/page.html">External</a>'
                "</article>",
                encoding="utf-8",
            )
            navigation = collection_navigation(destination)

            self.assertEqual(len(navigation), 3)
            first = navigation[collection / "b.html"]
            middle = navigation[collection / "a.html"]
            last = navigation[collection / "c.html"]
            self.assertNotIn('rel="prev"', first)
            self.assertIn('rel="next" href="a.html"', first)
            self.assertIn('rel="prev" href="b.html"', middle)
            self.assertIn("B &amp; first", middle)
            self.assertIn('rel="next" href="c.html"', middle)
            self.assertNotIn('rel="next"', last)
            for bar in navigation.values():
                self.assertIn('href="index.html"', bar)
                self.assertIn('aria-label="Talk navigation"', bar)
                self.assertEqual(PAGE_NAVIGATION.sub("", bar), "")


class VideoPlayerTests(unittest.TestCase):
    """Check video replacement without changing other content."""

    def test_player_preserves_fallback_and_is_idempotent(self) -> None:
        video_id = "FlTb383gXbU"
        fallback = (
            f'<a href="https://www.youtube.com/watch?v={video_id}">'
            "Watch on YouTube</a>"
        )
        original = (
            f'<p><a href="https://www.youtube.com/watch?v={video_id}">'
            f'<img src="https://img.youtube.com/vi/{video_id}/hqdefault.jpg"'
            ' alt="Video thumbnail"></a></p>'
            f"<p>{fallback}</p>"
        )

        result = embed_videos(original)

        self.assertIn(f'src="https://www.youtube-nocookie.com/embed/{video_id}"', result)
        self.assertIn('title="YouTube video player"', result)
        self.assertIn('loading="lazy"', result)
        self.assertIn("allowfullscreen", result)
        self.assertIn(fallback, result)
        self.assertNotIn("<img", result)
        self.assertEqual(result.count("<iframe"), 1)
        self.assertEqual(embed_videos(result), result)

    def test_other_links_and_images_are_unchanged(self) -> None:
        for html in (
            '<a href="https://www.youtube.com/watch?v=FlTb383gXbU">Recording</a>',
            '<img src="diagram.png" alt="Diagram">',
            '<a href="https://example.com/watch?v=FlTb383gXbU">'
            '<img src="https://img.youtube.com/vi/FlTb383gXbU/hqdefault.jpg"'
            ' alt="Video thumbnail"></a>',
            '<a href="https://www.youtube.com/watch?v=FlTb383gXbU">'
            '<img src="https://img.youtube.com/vi/AAAAAAAAAAA/hqdefault.jpg"'
            ' alt="Video thumbnail"></a>',
        ):
            with self.subTest(html=html):
                self.assertEqual(embed_videos(html), html)


if __name__ == "__main__":
    unittest.main()
