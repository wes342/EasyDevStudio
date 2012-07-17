.class Lcom/android/calculator2/Logic;
.super Ljava/lang/Object;
.source "Logic.java"


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/calculator2/Logic$Listener;
    }
.end annotation


# static fields
.field public static final DELETE_MODE_BACKSPACE:I = 0x0

.field public static final DELETE_MODE_CLEAR:I = 0x1

.field private static final INFINITY:Ljava/lang/String; = "Infinity"

.field private static final INFINITY_UNICODE:Ljava/lang/String; = "\u221e"

.field public static final MARKER_EVALUATE_ON_RESUME:Ljava/lang/String; = "?"

.field static final MINUS:C = '\u2212'

.field private static final NAN:Ljava/lang/String; = "NaN"

.field private static final ROUND_DIGITS:I = 0x1


# instance fields
.field private mDeleteMode:I

.field private mDisplay:Lcom/android/calculator2/CalculatorDisplay;

.field private final mErrorString:Ljava/lang/String;

.field private mHistory:Lcom/android/calculator2/History;

.field private mIsError:Z

.field private mLineLength:I

.field private mListener:Lcom/android/calculator2/Logic$Listener;

.field private mResult:Ljava/lang/String;

.field private mSymbols:Lorg/javia/arity/Symbols;


# direct methods
.method constructor <init>(Landroid/content/Context;Lcom/android/calculator2/History;Lcom/android/calculator2/CalculatorDisplay;)V
    .locals 2
    .parameter "context"
    .parameter "history"
    .parameter "display"

    .prologue
    const/4 v1, 0x0

    .line 64
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 34
    new-instance v0, Lorg/javia/arity/Symbols;

    invoke-direct {v0}, Lorg/javia/arity/Symbols;-><init>()V

    iput-object v0, p0, Lcom/android/calculator2/Logic;->mSymbols:Lorg/javia/arity/Symbols;

    .line 36
    const-string v0, ""

    iput-object v0, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    .line 37
    iput-boolean v1, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    .line 38
    iput v1, p0, Lcom/android/calculator2/Logic;->mLineLength:I

    .line 56
    iput v1, p0, Lcom/android/calculator2/Logic;->mDeleteMode:I

    .line 65
    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x7f080001

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/calculator2/Logic;->mErrorString:Ljava/lang/String;

    .line 66
    iput-object p2, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    .line 67
    iput-object p3, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    .line 68
    iget-object v0, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-virtual {v0, p0}, Lcom/android/calculator2/CalculatorDisplay;->setLogic(Lcom/android/calculator2/Logic;)V

    .line 69
    return-void
.end method

.method private clear(Z)V
    .locals 3
    .parameter "scroll"

    .prologue
    .line 130
    iget-object v0, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    const-string v1, ""

    invoke-virtual {v0, v1}, Lcom/android/calculator2/History;->enter(Ljava/lang/String;)V

    .line 131
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    const-string v2, ""

    if-eqz p1, :cond_0

    sget-object v0, Lcom/android/calculator2/CalculatorDisplay$Scroll;->UP:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    :goto_0
    invoke-virtual {v1, v2, v0}, Lcom/android/calculator2/CalculatorDisplay;->setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 132
    invoke-virtual {p0}, Lcom/android/calculator2/Logic;->cleared()V

    .line 133
    return-void

    .line 131
    :cond_0
    sget-object v0, Lcom/android/calculator2/CalculatorDisplay$Scroll;->NONE:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    goto :goto_0
.end method

.method private clearWithHistory(Z)V
    .locals 3
    .parameter "scroll"

    .prologue
    .line 114
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1}, Lcom/android/calculator2/History;->getText()Ljava/lang/String;

    move-result-object v0

    .line 115
    .local v0, text:Ljava/lang/String;
    const-string v1, "?"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_1

    .line 116
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1}, Lcom/android/calculator2/History;->moveToPrevious()Z

    move-result v1

    if-nez v1, :cond_0

    .line 117
    const-string v0, ""

    .line 119
    :cond_0
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1}, Lcom/android/calculator2/History;->getText()Ljava/lang/String;

    move-result-object v0

    .line 120
    sget-object v1, Lcom/android/calculator2/CalculatorDisplay$Scroll;->NONE:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    invoke-virtual {p0, v0, v1}, Lcom/android/calculator2/Logic;->evaluateAndShowResult(Ljava/lang/String;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 127
    :goto_0
    return-void

    .line 122
    :cond_1
    const-string v1, ""

    iput-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    .line 123
    iget-object v2, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    if-eqz p1, :cond_2

    sget-object v1, Lcom/android/calculator2/CalculatorDisplay$Scroll;->UP:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    :goto_1
    invoke-virtual {v2, v0, v1}, Lcom/android/calculator2/CalculatorDisplay;->setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 125
    const/4 v1, 0x0

    iput-boolean v1, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    goto :goto_0

    .line 123
    :cond_2
    sget-object v1, Lcom/android/calculator2/CalculatorDisplay$Scroll;->NONE:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    goto :goto_1
.end method

.method private getText()Ljava/lang/String;
    .locals 1

    .prologue
    .line 97
    iget-object v0, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-virtual {v0}, Lcom/android/calculator2/CalculatorDisplay;->getText()Landroid/text/Editable;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method static isOperator(C)Z
    .locals 2
    .parameter "c"

    .prologue
    .line 298
    const-string v0, "+\u2212\u00d7\u00f7/*"

    invoke-virtual {v0, p0}, Ljava/lang/String;->indexOf(I)I

    move-result v0

    const/4 v1, -0x1

    if-eq v0, v1, :cond_0

    const/4 v0, 0x1

    :goto_0
    return v0

    :cond_0
    const/4 v0, 0x0

    goto :goto_0
.end method

.method static isOperator(Ljava/lang/String;)Z
    .locals 3
    .parameter "text"

    .prologue
    const/4 v0, 0x1

    const/4 v1, 0x0

    .line 293
    invoke-virtual {p0}, Ljava/lang/String;->length()I

    move-result v2

    if-ne v2, v0, :cond_0

    invoke-virtual {p0, v1}, Ljava/lang/String;->charAt(I)C

    move-result v2

    invoke-static {v2}, Lcom/android/calculator2/Logic;->isOperator(C)Z

    move-result v2

    if-eqz v2, :cond_0

    :goto_0
    return v0

    :cond_0
    move v0, v1

    goto :goto_0
.end method

.method private tryFormattingWithPrecision(DI)Ljava/lang/String;
    .locals 10
    .parameter "value"
    .parameter "precision"

    .prologue
    .line 249
    sget-object v5, Ljava/util/Locale;->US:Ljava/util/Locale;

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "%"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    iget v7, p0, Lcom/android/calculator2/Logic;->mLineLength:I

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, "."

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, "g"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    const/4 v7, 0x1

    new-array v7, v7, [Ljava/lang/Object;

    const/4 v8, 0x0

    invoke-static {p1, p2}, Ljava/lang/Double;->valueOf(D)Ljava/lang/Double;

    move-result-object v9

    aput-object v9, v7, v8

    invoke-static {v5, v6, v7}, Ljava/lang/String;->format(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v4

    .line 250
    .local v4, result:Ljava/lang/String;
    const-string v5, "NaN"

    invoke-virtual {v4, v5}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_0

    .line 251
    const/4 v5, 0x1

    iput-boolean v5, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    .line 252
    iget-object v5, p0, Lcom/android/calculator2/Logic;->mErrorString:Ljava/lang/String;

    .line 289
    :goto_0
    return-object v5

    .line 254
    :cond_0
    move-object v2, v4

    .line 255
    .local v2, mantissa:Ljava/lang/String;
    const/4 v1, 0x0

    .line 256
    .local v1, exponent:Ljava/lang/String;
    const/16 v5, 0x65

    invoke-virtual {v4, v5}, Ljava/lang/String;->indexOf(I)I

    move-result v0

    .line 257
    .local v0, e:I
    const/4 v5, -0x1

    if-eq v0, v5, :cond_3

    .line 258
    const/4 v5, 0x0

    invoke-virtual {v4, v5, v0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v2

    .line 261
    add-int/lit8 v5, v0, 0x1

    invoke-virtual {v4, v5}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v1

    .line 262
    const-string v5, "+"

    invoke-virtual {v1, v5}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_1

    .line 263
    const/4 v5, 0x1

    invoke-virtual {v1, v5}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v1

    .line 265
    :cond_1
    invoke-static {v1}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v5

    invoke-static {v5}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    .line 270
    :goto_1
    const/16 v5, 0x2e

    invoke-virtual {v2, v5}, Ljava/lang/String;->indexOf(I)I

    move-result v3

    .line 271
    .local v3, period:I
    const/4 v5, -0x1

    if-ne v3, v5, :cond_2

    .line 272
    const/16 v5, 0x2c

    invoke-virtual {v2, v5}, Ljava/lang/String;->indexOf(I)I

    move-result v3

    .line 274
    :cond_2
    const/4 v5, -0x1

    if-eq v3, v5, :cond_5

    .line 276
    :goto_2
    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v5

    if-lez v5, :cond_4

    const-string v5, "0"

    invoke-virtual {v2, v5}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_4

    .line 277
    const/4 v5, 0x0

    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v6

    add-int/lit8 v6, v6, -0x1

    invoke-virtual {v2, v5, v6}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v2

    goto :goto_2

    .line 267
    .end local v3           #period:I
    :cond_3
    move-object v2, v4

    goto :goto_1

    .line 279
    .restart local v3       #period:I
    :cond_4
    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v5

    add-int/lit8 v6, v3, 0x1

    if-ne v5, v6, :cond_5

    .line 280
    const/4 v5, 0x0

    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v6

    add-int/lit8 v6, v6, -0x1

    invoke-virtual {v2, v5, v6}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v2

    .line 284
    :cond_5
    if-eqz v1, :cond_6

    .line 285
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    const/16 v6, 0x65

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    :goto_3
    move-object v5, v4

    .line 289
    goto/16 :goto_0

    .line 287
    :cond_6
    move-object v4, v2

    goto :goto_3
.end method


# virtual methods
.method acceptInsert(Ljava/lang/String;)Z
    .locals 3
    .parameter "delta"

    .prologue
    .line 144
    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v0

    .line 145
    .local v0, text:Ljava/lang/String;
    iget-boolean v1, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    if-nez v1, :cond_1

    iget-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-static {p1}, Lcom/android/calculator2/Logic;->isOperator(Ljava/lang/String;)Z

    move-result v1

    if-nez v1, :cond_0

    iget-object v1, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-virtual {v1}, Lcom/android/calculator2/CalculatorDisplay;->getSelectionStart()I

    move-result v1

    invoke-virtual {v0}, Ljava/lang/String;->length()I

    move-result v2

    if-eq v1, v2, :cond_1

    :cond_0
    const/4 v1, 0x1

    :goto_0
    return v1

    :cond_1
    const/4 v1, 0x0

    goto :goto_0
.end method

.method cleared()V
    .locals 2

    .prologue
    const/4 v1, 0x0

    .line 136
    const-string v0, ""

    iput-object v0, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    .line 137
    iput-boolean v1, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    .line 138
    invoke-virtual {p0}, Lcom/android/calculator2/Logic;->updateHistory()V

    .line 140
    invoke-virtual {p0, v1}, Lcom/android/calculator2/Logic;->setDeleteMode(I)V

    .line 141
    return-void
.end method

.method eatHorizontalMove(Z)Z
    .locals 5
    .parameter "toLeft"

    .prologue
    const/4 v2, 0x1

    const/4 v3, 0x0

    .line 91
    iget-object v4, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-virtual {v4}, Lcom/android/calculator2/CalculatorDisplay;->getEditText()Landroid/widget/EditText;

    move-result-object v1

    .line 92
    .local v1, editText:Landroid/widget/EditText;
    invoke-virtual {v1}, Landroid/widget/EditText;->getSelectionStart()I

    move-result v0

    .line 93
    .local v0, cursorPos:I
    if-eqz p1, :cond_2

    if-nez v0, :cond_1

    :cond_0
    :goto_0
    return v2

    :cond_1
    move v2, v3

    goto :goto_0

    :cond_2
    invoke-virtual {v1}, Landroid/widget/EditText;->length()I

    move-result v4

    if-ge v0, v4, :cond_0

    move v2, v3

    goto :goto_0
.end method

.method evaluate(Ljava/lang/String;)Ljava/lang/String;
    .locals 8
    .parameter "input"
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Lorg/javia/arity/SyntaxException;
        }
    .end annotation

    .prologue
    .line 223
    invoke-virtual {p1}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v5

    const-string v6, ""

    invoke-virtual {v5, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_0

    .line 224
    const-string v5, ""

    .line 243
    :goto_0
    return-object v5

    .line 228
    :cond_0
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v2

    .line 229
    .local v2, size:I
    :goto_1
    if-lez v2, :cond_1

    add-int/lit8 v5, v2, -0x1

    invoke-virtual {p1, v5}, Ljava/lang/String;->charAt(I)C

    move-result v5

    invoke-static {v5}, Lcom/android/calculator2/Logic;->isOperator(C)Z

    move-result v5

    if-eqz v5, :cond_1

    .line 230
    const/4 v5, 0x0

    add-int/lit8 v6, v2, -0x1

    invoke-virtual {p1, v5, v6}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p1

    .line 231
    add-int/lit8 v2, v2, -0x1

    goto :goto_1

    .line 234
    :cond_1
    iget-object v5, p0, Lcom/android/calculator2/Logic;->mSymbols:Lorg/javia/arity/Symbols;

    invoke-virtual {v5, p1}, Lorg/javia/arity/Symbols;->eval(Ljava/lang/String;)D

    move-result-wide v3

    .line 236
    .local v3, value:D
    const-string v1, ""

    .line 237
    .local v1, result:Ljava/lang/String;
    iget v0, p0, Lcom/android/calculator2/Logic;->mLineLength:I

    .local v0, precision:I
    :goto_2
    const/4 v5, 0x6

    if-le v0, v5, :cond_2

    .line 238
    invoke-direct {p0, v3, v4, v0}, Lcom/android/calculator2/Logic;->tryFormattingWithPrecision(DI)Ljava/lang/String;

    move-result-object v1

    .line 239
    invoke-virtual {v1}, Ljava/lang/String;->length()I

    move-result v5

    iget v6, p0, Lcom/android/calculator2/Logic;->mLineLength:I

    if-gt v5, v6, :cond_3

    .line 243
    :cond_2
    const/16 v5, 0x2d

    const/16 v6, 0x2212

    invoke-virtual {v1, v5, v6}, Ljava/lang/String;->replace(CC)Ljava/lang/String;

    move-result-object v5

    const-string v6, "Infinity"

    const-string v7, "\u221e"

    invoke-virtual {v5, v6, v7}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v5

    goto :goto_0

    .line 237
    :cond_3
    add-int/lit8 v0, v0, -0x1

    goto :goto_2
.end method

.method public evaluateAndShowResult(Ljava/lang/String;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V
    .locals 5
    .parameter "text"
    .parameter "scroll"

    .prologue
    const/4 v4, 0x1

    .line 174
    :try_start_0
    invoke-virtual {p0, p1}, Lcom/android/calculator2/Logic;->evaluate(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    .line 175
    .local v1, result:Ljava/lang/String;
    invoke-virtual {p1, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_0

    .line 176
    iget-object v2, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v2, p1}, Lcom/android/calculator2/History;->enter(Ljava/lang/String;)V

    .line 177
    iput-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    .line 178
    iget-object v2, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    iget-object v3, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v2, v3, p2}, Lcom/android/calculator2/CalculatorDisplay;->setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 179
    const/4 v2, 0x1

    invoke-virtual {p0, v2}, Lcom/android/calculator2/Logic;->setDeleteMode(I)V
    :try_end_0
    .catch Lorg/javia/arity/SyntaxException; {:try_start_0 .. :try_end_0} :catch_0

    .line 187
    .end local v1           #result:Ljava/lang/String;
    :cond_0
    :goto_0
    return-void

    .line 181
    :catch_0
    move-exception v0

    .line 182
    .local v0, e:Lorg/javia/arity/SyntaxException;
    iput-boolean v4, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    .line 183
    iget-object v2, p0, Lcom/android/calculator2/Logic;->mErrorString:Ljava/lang/String;

    iput-object v2, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    .line 184
    iget-object v2, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    iget-object v3, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v2, v3, p2}, Lcom/android/calculator2/CalculatorDisplay;->setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 185
    invoke-virtual {p0, v4}, Lcom/android/calculator2/Logic;->setDeleteMode(I)V

    goto :goto_0
.end method

.method public getDeleteMode()I
    .locals 1

    .prologue
    .line 83
    iget v0, p0, Lcom/android/calculator2/Logic;->mDeleteMode:I

    return v0
.end method

.method insert(Ljava/lang/String;)V
    .locals 1
    .parameter "delta"

    .prologue
    .line 101
    iget-object v0, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-virtual {v0, p1}, Lcom/android/calculator2/CalculatorDisplay;->insert(Ljava/lang/String;)V

    .line 102
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/calculator2/Logic;->setDeleteMode(I)V

    .line 103
    return-void
.end method

.method onClear()V
    .locals 2

    .prologue
    const/4 v0, 0x1

    .line 161
    iget v1, p0, Lcom/android/calculator2/Logic;->mDeleteMode:I

    if-ne v1, v0, :cond_0

    :goto_0
    invoke-direct {p0, v0}, Lcom/android/calculator2/Logic;->clear(Z)V

    .line 162
    return-void

    .line 161
    :cond_0
    const/4 v0, 0x0

    goto :goto_0
.end method

.method onDelete()V
    .locals 4

    .prologue
    const/4 v3, 0x0

    .line 152
    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    iget-boolean v0, p0, Lcom/android/calculator2/Logic;->mIsError:Z

    if-eqz v0, :cond_1

    .line 153
    :cond_0
    invoke-direct {p0, v3}, Lcom/android/calculator2/Logic;->clear(Z)V

    .line 158
    :goto_0
    return-void

    .line 155
    :cond_1
    iget-object v0, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    new-instance v1, Landroid/view/KeyEvent;

    const/16 v2, 0x43

    invoke-direct {v1, v3, v2}, Landroid/view/KeyEvent;-><init>(II)V

    invoke-virtual {v0, v1}, Lcom/android/calculator2/CalculatorDisplay;->dispatchKeyEvent(Landroid/view/KeyEvent;)Z

    .line 156
    const-string v0, ""

    iput-object v0, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    goto :goto_0
.end method

.method onDown()V
    .locals 4

    .prologue
    .line 200
    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v0

    .line 201
    .local v0, text:Ljava/lang/String;
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_0

    .line 202
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1, v0}, Lcom/android/calculator2/History;->update(Ljava/lang/String;)V

    .line 204
    :cond_0
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1}, Lcom/android/calculator2/History;->moveToNext()Z

    move-result v1

    if-eqz v1, :cond_1

    .line 205
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    iget-object v2, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v2}, Lcom/android/calculator2/History;->getText()Ljava/lang/String;

    move-result-object v2

    sget-object v3, Lcom/android/calculator2/CalculatorDisplay$Scroll;->UP:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    invoke-virtual {v1, v2, v3}, Lcom/android/calculator2/CalculatorDisplay;->setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 207
    :cond_1
    return-void
.end method

.method onEnter()V
    .locals 2

    .prologue
    .line 165
    iget v0, p0, Lcom/android/calculator2/Logic;->mDeleteMode:I

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    .line 166
    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lcom/android/calculator2/Logic;->clearWithHistory(Z)V

    .line 170
    :goto_0
    return-void

    .line 168
    :cond_0
    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v0

    sget-object v1, Lcom/android/calculator2/CalculatorDisplay$Scroll;->UP:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    invoke-virtual {p0, v0, v1}, Lcom/android/calculator2/Logic;->evaluateAndShowResult(Ljava/lang/String;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    goto :goto_0
.end method

.method public onTextChanged()V
    .locals 1

    .prologue
    .line 106
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/calculator2/Logic;->setDeleteMode(I)V

    .line 107
    return-void
.end method

.method onUp()V
    .locals 4

    .prologue
    .line 190
    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v0

    .line 191
    .local v0, text:Ljava/lang/String;
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_0

    .line 192
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1, v0}, Lcom/android/calculator2/History;->update(Ljava/lang/String;)V

    .line 194
    :cond_0
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v1}, Lcom/android/calculator2/History;->moveToPrevious()Z

    move-result v1

    if-eqz v1, :cond_1

    .line 195
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    iget-object v2, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v2}, Lcom/android/calculator2/History;->getText()Ljava/lang/String;

    move-result-object v2

    sget-object v3, Lcom/android/calculator2/CalculatorDisplay$Scroll;->DOWN:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    invoke-virtual {v1, v2, v3}, Lcom/android/calculator2/CalculatorDisplay;->setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V

    .line 197
    :cond_1
    return-void
.end method

.method public resumeWithHistory()V
    .locals 1

    .prologue
    .line 110
    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lcom/android/calculator2/Logic;->clearWithHistory(Z)V

    .line 111
    return-void
.end method

.method public setDeleteMode(I)V
    .locals 1
    .parameter "mode"

    .prologue
    .line 76
    iget v0, p0, Lcom/android/calculator2/Logic;->mDeleteMode:I

    if-eq v0, p1, :cond_0

    .line 77
    iput p1, p0, Lcom/android/calculator2/Logic;->mDeleteMode:I

    .line 78
    iget-object v0, p0, Lcom/android/calculator2/Logic;->mListener:Lcom/android/calculator2/Logic$Listener;

    invoke-interface {v0}, Lcom/android/calculator2/Logic$Listener;->onDeleteModeChange()V

    .line 80
    :cond_0
    return-void
.end method

.method setLineLength(I)V
    .locals 0
    .parameter "nDigits"

    .prologue
    .line 87
    iput p1, p0, Lcom/android/calculator2/Logic;->mLineLength:I

    .line 88
    return-void
.end method

.method public setListener(Lcom/android/calculator2/Logic$Listener;)V
    .locals 0
    .parameter "listener"

    .prologue
    .line 72
    iput-object p1, p0, Lcom/android/calculator2/Logic;->mListener:Lcom/android/calculator2/Logic$Listener;

    .line 73
    return-void
.end method

.method updateHistory()V
    .locals 3

    .prologue
    .line 210
    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v0

    .line 213
    .local v0, text:Ljava/lang/String;
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    iget-object v1, p0, Lcom/android/calculator2/Logic;->mErrorString:Ljava/lang/String;

    invoke-static {v0, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    iget-object v1, p0, Lcom/android/calculator2/Logic;->mResult:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_0

    .line 215
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    const-string v2, "?"

    invoke-virtual {v1, v2}, Lcom/android/calculator2/History;->update(Ljava/lang/String;)V

    .line 219
    :goto_0
    return-void

    .line 217
    :cond_0
    iget-object v1, p0, Lcom/android/calculator2/Logic;->mHistory:Lcom/android/calculator2/History;

    invoke-direct {p0}, Lcom/android/calculator2/Logic;->getText()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/calculator2/History;->update(Ljava/lang/String;)V

    goto :goto_0
.end method
