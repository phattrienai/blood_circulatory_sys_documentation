# Sphinx: Basic Guide for Writing `.rst` Files

This guide introduces the basics of writing **reStructuredText (`.rst`)** files for **Sphinx**, from fundamentals to practical usage. It is suitable for beginners writing technical documentation.

---

## 1. What is a `.rst` File?

- `.rst` stands for **reStructuredText**
- It is the default markup language used by **Sphinx**
- Commonly used for:
  - Python documentation
  - API documentation
  - Technical guides and tutorials

---

## 2. Basic Structure of an `.rst` File

Example: `index.rst`

```rst
Project Title
=============

Welcome to the documentation!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   intro
   install
   usage
```

**Important rules**
- The underline must match the title length
- Indentation is critical in `.rst`

---

## 3. Headings

```rst
Level 1
=======

Level 2
-------

Level 3
~~~~~~~

Level 4
^^^^^^^
```

Be consistent throughout the project.

---

## 4. Paragraphs & Line Breaks

```rst
This is a paragraph.

This is another paragraph.
```

- A blank line separates paragraphs
- Do not manually break lines within a paragraph

---

## 5. Bold, Italic, Inline Code

```rst
**bold text**
*italic text*
``inline code``
```

---

## 6. Lists

### 6.1 Unordered Lists

```rst
- Item 1
- Item 2
  - Sub item
```

### 6.2 Ordered Lists

```rst
1. First
2. Second
3. Third
```

---

## 7. Code Blocks

### 7.1 Basic Code Block

```rst
::

   print("Hello World")
```

### 7.2 Code Block with Syntax Highlighting

```rst
.. code-block:: python

   def hello():
       print("Hello")
```

---

## 8. Links & References

### 8.1 Inline Links

```rst
`Python <https://www.python.org>`_
```

### 8.2 Reference Links

```rst
Visit the `Python`_ website.

.. _Python: https://www.python.org
```

---

## 9. Images

```rst
.. image:: images/logo.png
   :alt: Logo
   :width: 200px
   :align: center
```

---

## 10. Admonitions

```rst
.. note::
   This is a note.

.. warning::
   Be careful!

.. tip::
   Useful tip.
```

---

## 11. Tables

### Simple Table

```rst
=====  =====
Name   Age
=====  =====
Alice  20
Bob    30
=====  =====
```

---

## 12. toctree

```rst
.. toctree::
   :maxdepth: 2
   :caption: Guides

   intro
   install
   usage
```

---

## 13. Cross References

```rst
See :ref:`installation`.

.. _installation:

Installation
------------
```

---

## 14. Python API Documentation

```rst
.. automodule:: mypackage.mymodule
   :members:
   :undoc-members:
```

---

## 15. Build Commands

```bash
sphinx-quickstart
make html
```

---

## 16. Common Errors

| Error | Cause |
|------|------|
| Unexpected indentation | Incorrect spacing |
| Code not rendered | Missing blank line |
| toctree file not found | Wrong filename |
| Duplicate label | Duplicate labels |

---

## 17. Best Practices

- One file per topic
- Prefer code-block
- Keep headings consistent
- Write docs early

---

## 18. Minimal Example

```rst
My Project
==========

.. toctree::
   :maxdepth: 1

   intro

Introduction
------------

This is **Sphinx** documentation.

.. code-block:: python

   print("Hello Sphinx")
```
