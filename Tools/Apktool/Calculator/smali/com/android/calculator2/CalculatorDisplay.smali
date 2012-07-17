.class Lcom/android/calculator2/CalculatorDisplay;
.super Landroid/widget/ViewSwitcher;
.source "CalculatorDisplay.java"


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/calculator2/CalculatorDisplay$Scroll;
    }
.end annotation


# static fields
.field private static final ACCEPTED_CHARS:[C = null

.field private static final ANIM_DURATION:I = 0x1f4

.field private static final ATTR_MAX_DIGITS:Ljava/lang/String; = "maxDigits"

.field private static final DEFAULT_MAX_DIGITS:I = 0xa


# instance fields
.field inAnimDown:Landroid/view/animation/TranslateAnimation;

.field inAnimUp:Landroid/view/animation/TranslateAnimation;

.field private mLogic:Lcom/android/calculator2/Logic;

.field private mMaxDigits:I

.field outAnimDown:Landroid/view/animation/TranslateAnimation;

.field outAnimUp:Landroid/view/animation/TranslateAnimation;


# direct methods
.method static constructor <clinit>()V
    .locals 1

    .prologue
    .line 39
    const-string v0, "0123456789.+-*/\u2212\u00d7\u00f7()!%^"

    invoke-virtual {v0}, Ljava/lang/String;->toCharArray()[C

    move-result-object v0

    sput-object v0, Lcom/android/calculator2/CalculatorDisplay;->ACCEPTED_CHARS:[C

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .locals 3
    .parameter "context"
    .parameter "attrs"

    .prologue
    const/16 v2, 0xa

    .line 55
    invoke-direct {p0, p1, p2}, Landroid/widget/ViewSwitcher;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    .line 52
    iput v2, p0, Lcom/android/calculator2/CalculatorDisplay;->mMaxDigits:I

    .line 56
    const/4 v0, 0x0

    const-string v1, "maxDigits"

    invoke-interface {p2, v0, v1, v2}, Landroid/util/AttributeSet;->getAttributeIntValue(Ljava/lang/String;Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/calculator2/CalculatorDisplay;->mMaxDigits:I

    .line 57
    return-void
.end method

.method static synthetic access$000()[C
    .locals 1

    .prologue
    .line 33
    sget-object v0, Lcom/android/calculator2/CalculatorDisplay;->ACCEPTED_CHARS:[C

    return-object v0
.end method


# virtual methods
.method getEditText()Landroid/widget/EditText;
    .locals 1

    .prologue
    .line 122
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->getCurrentView()Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    return-object v0
.end method

.method public getMaxDigits()I
    .locals 1

    .prologue
    .line 60
    iget v0, p0, Lcom/android/calculator2/CalculatorDisplay;->mMaxDigits:I

    return v0
.end method

.method getSelectionStart()I
    .locals 2

    .prologue
    .line 154
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->getCurrentView()Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    .line 155
    .local v0, text:Landroid/widget/EditText;
    invoke-virtual {v0}, Landroid/widget/EditText;->getSelectionStart()I

    move-result v1

    return v1
.end method

.method getText()Landroid/text/Editable;
    .locals 2

    .prologue
    .line 126
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->getCurrentView()Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    .line 127
    .local v0, text:Landroid/widget/EditText;
    invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v1

    return-object v1
.end method

.method insert(Ljava/lang/String;)V
    .locals 3
    .parameter "delta"

    .prologue
    .line 116
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->getCurrentView()Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/EditText;

    .line 117
    .local v1, editor:Landroid/widget/EditText;
    invoke-virtual {v1}, Landroid/widget/EditText;->getSelectionStart()I

    move-result v0

    .line 118
    .local v0, cursor:I
    invoke-virtual {v1}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v2

    invoke-interface {v2, v0, p1}, Landroid/text/Editable;->insert(ILjava/lang/CharSequence;)Landroid/text/Editable;

    .line 119
    return-void
.end method

.method protected onFocusChanged(ZILandroid/graphics/Rect;)V
    .locals 0
    .parameter "gain"
    .parameter "direction"
    .parameter "prev"

    .prologue
    .line 161
    if-nez p1, :cond_0

    .line 162
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->requestFocus()Z

    .line 164
    :cond_0
    return-void
.end method

.method protected onSizeChanged(IIII)V
    .locals 5
    .parameter "w"
    .parameter "h"
    .parameter "oldW"
    .parameter "oldH"

    .prologue
    const-wide/16 v3, 0x1f4

    const/4 v2, 0x0

    .line 104
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    int-to-float v1, p2

    invoke-direct {v0, v2, v2, v1, v2}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->inAnimUp:Landroid/view/animation/TranslateAnimation;

    .line 105
    iget-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->inAnimUp:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 106
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    neg-int v1, p2

    int-to-float v1, v1

    invoke-direct {v0, v2, v2, v2, v1}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->outAnimUp:Landroid/view/animation/TranslateAnimation;

    .line 107
    iget-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->outAnimUp:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 109
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    neg-int v1, p2

    int-to-float v1, v1

    invoke-direct {v0, v2, v2, v1, v2}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->inAnimDown:Landroid/view/animation/TranslateAnimation;

    .line 110
    iget-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->inAnimDown:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 111
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    int-to-float v1, p2

    invoke-direct {v0, v2, v2, v2, v1}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->outAnimDown:Landroid/view/animation/TranslateAnimation;

    .line 112
    iget-object v0, p0, Lcom/android/calculator2/CalculatorDisplay;->outAnimDown:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 113
    return-void
.end method

.method protected setLogic(Lcom/android/calculator2/Logic;)V
    .locals 5
    .parameter "logic"

    .prologue
    .line 64
    iput-object p1, p0, Lcom/android/calculator2/CalculatorDisplay;->mLogic:Lcom/android/calculator2/Logic;

    .line 65
    new-instance v0, Lcom/android/calculator2/CalculatorDisplay$1;

    invoke-direct {v0, p0}, Lcom/android/calculator2/CalculatorDisplay$1;-><init>(Lcom/android/calculator2/CalculatorDisplay;)V

    .line 86
    .local v0, calculatorKeyListener:Landroid/text/method/NumberKeyListener;
    new-instance v1, Lcom/android/calculator2/CalculatorEditable$Factory;

    invoke-direct {v1, p1}, Lcom/android/calculator2/CalculatorEditable$Factory;-><init>(Lcom/android/calculator2/Logic;)V

    .line 87
    .local v1, factory:Landroid/text/Editable$Factory;
    const/4 v2, 0x0

    .local v2, i:I
    :goto_0
    const/4 v4, 0x2

    if-ge v2, v4, :cond_0

    .line 88
    invoke-virtual {p0, v2}, Lcom/android/calculator2/CalculatorDisplay;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    check-cast v3, Landroid/widget/EditText;

    .line 89
    .local v3, text:Landroid/widget/EditText;
    const/4 v4, 0x0

    invoke-virtual {v3, v4}, Landroid/widget/EditText;->setBackgroundDrawable(Landroid/graphics/drawable/Drawable;)V

    .line 90
    invoke-virtual {v3, v1}, Landroid/widget/EditText;->setEditableFactory(Landroid/text/Editable$Factory;)V

    .line 91
    invoke-virtual {v3, v0}, Landroid/widget/EditText;->setKeyListener(Landroid/text/method/KeyListener;)V

    .line 92
    invoke-virtual {v3}, Landroid/widget/EditText;->setSingleLine()V

    .line 87
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    .line 94
    .end local v3           #text:Landroid/widget/EditText;
    :cond_0
    return-void
.end method

.method public setOnKeyListener(Landroid/view/View$OnKeyListener;)V
    .locals 1
    .parameter "l"

    .prologue
    .line 98
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/calculator2/CalculatorDisplay;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0, p1}, Landroid/view/View;->setOnKeyListener(Landroid/view/View$OnKeyListener;)V

    .line 99
    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lcom/android/calculator2/CalculatorDisplay;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0, p1}, Landroid/view/View;->setOnKeyListener(Landroid/view/View$OnKeyListener;)V

    .line 100
    return-void
.end method

.method setText(Ljava/lang/CharSequence;Lcom/android/calculator2/CalculatorDisplay$Scroll;)V
    .locals 3
    .parameter "text"
    .parameter "dir"

    .prologue
    const/4 v2, 0x0

    .line 131
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->getText()Landroid/text/Editable;

    move-result-object v1

    invoke-interface {v1}, Landroid/text/Editable;->length()I

    move-result v1

    if-nez v1, :cond_0

    .line 132
    sget-object p2, Lcom/android/calculator2/CalculatorDisplay$Scroll;->NONE:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    .line 135
    :cond_0
    sget-object v1, Lcom/android/calculator2/CalculatorDisplay$Scroll;->UP:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    if-ne p2, v1, :cond_1

    .line 136
    iget-object v1, p0, Lcom/android/calculator2/CalculatorDisplay;->inAnimUp:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {p0, v1}, Lcom/android/calculator2/CalculatorDisplay;->setInAnimation(Landroid/view/animation/Animation;)V

    .line 137
    iget-object v1, p0, Lcom/android/calculator2/CalculatorDisplay;->outAnimUp:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {p0, v1}, Lcom/android/calculator2/CalculatorDisplay;->setOutAnimation(Landroid/view/animation/Animation;)V

    .line 146
    :goto_0
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->getNextView()Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    .line 147
    .local v0, editText:Landroid/widget/EditText;
    invoke-virtual {v0, p1}, Landroid/widget/EditText;->setText(Ljava/lang/CharSequence;)V

    .line 149
    invoke-interface {p1}, Ljava/lang/CharSequence;->length()I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/EditText;->setSelection(I)V

    .line 150
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorDisplay;->showNext()V

    .line 151
    return-void

    .line 138
    .end local v0           #editText:Landroid/widget/EditText;
    :cond_1
    sget-object v1, Lcom/android/calculator2/CalculatorDisplay$Scroll;->DOWN:Lcom/android/calculator2/CalculatorDisplay$Scroll;

    if-ne p2, v1, :cond_2

    .line 139
    iget-object v1, p0, Lcom/android/calculator2/CalculatorDisplay;->inAnimDown:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {p0, v1}, Lcom/android/calculator2/CalculatorDisplay;->setInAnimation(Landroid/view/animation/Animation;)V

    .line 140
    iget-object v1, p0, Lcom/android/calculator2/CalculatorDisplay;->outAnimDown:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {p0, v1}, Lcom/android/calculator2/CalculatorDisplay;->setOutAnimation(Landroid/view/animation/Animation;)V

    goto :goto_0

    .line 142
    :cond_2
    invoke-virtual {p0, v2}, Lcom/android/calculator2/CalculatorDisplay;->setInAnimation(Landroid/view/animation/Animation;)V

    .line 143
    invoke-virtual {p0, v2}, Lcom/android/calculator2/CalculatorDisplay;->setOutAnimation(Landroid/view/animation/Animation;)V

    goto :goto_0
.end method
