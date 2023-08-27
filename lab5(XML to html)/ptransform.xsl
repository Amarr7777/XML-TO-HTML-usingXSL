<!-- transform.xsl -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" />

    <xsl:template match="/products">
        <html>
            <head>
                <title>Product Catalog</title>
            </head>
            <body>
                <h1>Product Details</h1>
                <xsl:apply-templates select="product"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="product">
        <div class="product">
            <table border="1">
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Description</th>
                </tr>
                    <tr>
                        <td>
                            <xsl:value-of select="name" />
                        </td>
                        <td>
                            <xsl:value-of select="price" />
                        </td>
                        <td>
                            <xsl:value-of select="description" />
                        </td>
                    </tr>
            </table>
        </div>
    </xsl:template>
</xsl:stylesheet>