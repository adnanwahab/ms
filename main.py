from fasthtml.common import *

app, rt = fast_app(hdrs=(picolink))


@rt("/")
def get():
    return (


        Script("window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };"),
        Script(src="/_vercel/insights/script.js"),
        Script(src="https://cdn.tailwindcss.com"),
        Script("""
//import { inject } from '@vercel/analytics';
        //import { inject } from 'https://cdn.jsdelivr.com/npm/@vercel/analytics@latest/dist/analytics.js';
        import vercelanalytics from 'https://cdn.jsdelivr.net/npm/@vercel/analytics@1.3.1/+esm'
console.log(vercelanalytics)

vercelanalytics.inject();
console.log('penis');
        """, type="module"),
        Socials(
            title="Vercel + FastHTML + EGGNOG WABAH",
            site_name="Vercel",
            description="A demo of Vercel and FastHTML integration",
            image="https://vercel.fyi/fasthtml-og",
            url="https://fasthtml-template.vercel.app",
            twitter_site="@vercel",
        ),
        Container(
            Img(src="https://hashirama.blog/static/images/what_was_lost.jpeg", cls="animate-spin"),
            Card(
                Group(
                    P(
                        "FastHTML is a new next-generation web framework for fast, scalable web applications with minimal, compact code. It builds on top of popular foundations like ASGI and HTMX. You can now deploy FastHTML with Vercel CLI or by pushing new changes to your git repository.",
                    ),
                ),
                header=(Titled("FastHTML + Vercel")),
                footer=(
                    P(
                        A(
                            "Deploy your own",
                            href="https://vercel.com/templates/python/fasthtml-python-boilerplate",
                        ),
                        " or ",
                        A("learn more", href="https://docs.fastht.ml/"),
                        "about FastHTML.",
                    )
                ),
            ),
        ),
    )


serve()
