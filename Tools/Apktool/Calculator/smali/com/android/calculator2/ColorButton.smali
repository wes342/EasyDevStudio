.class Lcom/android/calculator2/ColorButton;
.super Landroid/widget/Button;
.source "ColorButton.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# static fields
.field static final CLICK_FEEDBACK_DURATION:I = 0x15e

.field static final CLICK_FEEDBACK_INTERVAL:I = 0xa


# instance fields
.field CLICK_FEEDBACK_COLOR:I

.field mAnimStart:J

.field mFeedbackPaint:Landroid/graphics/Paint;

.field mListener:Landroid/view/View$OnClickListener;

.field mTextX:F

.field mTextY:F


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .locals 2
    .parameter "context"
    .parameter "attrs"

    .prologue
    .line 45
    invoke-direct {p0, p1, p2}, Landroid/widget/Button;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    move-object v0, p1

    .line 46
    check-cast v0, Lcom/android/calculator2/Calculator;

    .line 47
    .local v0, calc:Lcom/android/calculator2/Calculator;
    invoke-direct {p0, v0}, Lcom/android/calculator2/ColorButton;->init(Lcom/android/calculator2/Calculator;)V

    .line 48
    iget-object v1, v0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    iput-object v1, p0, Lcom/android/calculator2/ColorButton;->mListener:Landroid/view/View$OnClickListener;

    .line 49
    invoke-virtual {p0, p0}, Lcom/android/calculator2/ColorButton;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 50
    return-void
.end method

.method private drawMagicFlame(ILandroid/graphics/Canvas;)V
    .locals 8
    .parameter "duration"
    .parameter "canvas"

    .prologue
    const/high16 v1, 0x3f80

    .line 86
    mul-int/lit16 v0, p1, 0xff

    div-int/lit16 v0, v0, 0x15e

    rsub-int v6, v0, 0xff

    .line 87
    .local v6, alpha:I
    iget v0, p0, Lcom/android/calculator2/ColorButton;->CLICK_FEEDBACK_COLOR:I

    shl-int/lit8 v2, v6, 0x18

    or-int v7, v0, v2

    .line 89
    .local v7, color:I
    iget-object v0, p0, Lcom/android/calculator2/ColorButton;->mFeedbackPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v7}, Landroid/graphics/Paint;->setColor(I)V

    .line 90
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getWidth()I

    move-result v0

    add-int/lit8 v0, v0, -0x1

    int-to-float v3, v0

    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getHeight()I

    move-result v0

    add-int/lit8 v0, v0, -0x1

    int-to-float v4, v0

    iget-object v5, p0, Lcom/android/calculator2/ColorButton;->mFeedbackPaint:Landroid/graphics/Paint;

    move-object v0, p2

    move v2, v1

    invoke-virtual/range {v0 .. v5}, Landroid/graphics/Canvas;->drawRect(FFFFLandroid/graphics/Paint;)V

    .line 91
    return-void
.end method

.method private init(Lcom/android/calculator2/Calculator;)V
    .locals 3
    .parameter "calc"

    .prologue
    .line 57
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    .line 59
    .local v0, res:Landroid/content/res/Resources;
    const/high16 v1, 0x7f06

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getColor(I)I

    move-result v1

    iput v1, p0, Lcom/android/calculator2/ColorButton;->CLICK_FEEDBACK_COLOR:I

    .line 60
    new-instance v1, Landroid/graphics/Paint;

    invoke-direct {v1}, Landroid/graphics/Paint;-><init>()V

    iput-object v1, p0, Lcom/android/calculator2/ColorButton;->mFeedbackPaint:Landroid/graphics/Paint;

    .line 61
    iget-object v1, p0, Lcom/android/calculator2/ColorButton;->mFeedbackPaint:Landroid/graphics/Paint;

    sget-object v2, Landroid/graphics/Paint$Style;->STROKE:Landroid/graphics/Paint$Style;

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V

    .line 62
    iget-object v1, p0, Lcom/android/calculator2/ColorButton;->mFeedbackPaint:Landroid/graphics/Paint;

    const/high16 v2, 0x4000

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    .line 63
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getPaint()Landroid/text/TextPaint;

    move-result-object v1

    const v2, 0x7f060001

    invoke-virtual {v0, v2}, Landroid/content/res/Resources;->getColor(I)I

    move-result v2

    invoke-virtual {v1, v2}, Landroid/text/TextPaint;->setColor(I)V

    .line 65
    const-wide/16 v1, -0x1

    iput-wide v1, p0, Lcom/android/calculator2/ColorButton;->mAnimStart:J

    .line 66
    return-void
.end method

.method private measureText()V
    .locals 4

    .prologue
    const/high16 v3, 0x4000

    .line 75
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    .line 76
    .local v0, paint:Landroid/graphics/Paint;
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getWidth()I

    move-result v1

    int-to-float v1, v1

    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getText()Ljava/lang/CharSequence;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v2

    sub-float/2addr v1, v2

    div-float/2addr v1, v3

    iput v1, p0, Lcom/android/calculator2/ColorButton;->mTextX:F

    .line 77
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getHeight()I

    move-result v1

    int-to-float v1, v1

    invoke-virtual {v0}, Landroid/graphics/Paint;->ascent()F

    move-result v2

    sub-float/2addr v1, v2

    invoke-virtual {v0}, Landroid/graphics/Paint;->descent()F

    move-result v2

    sub-float/2addr v1, v2

    div-float/2addr v1, v3

    iput v1, p0, Lcom/android/calculator2/ColorButton;->mTextY:F

    .line 78
    return-void
.end method


# virtual methods
.method public animateClickFeedback()V
    .locals 2

    .prologue
    .line 113
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    iput-wide v0, p0, Lcom/android/calculator2/ColorButton;->mAnimStart:J

    .line 114
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->invalidate()V

    .line 115
    return-void
.end method

.method public onClick(Landroid/view/View;)V
    .locals 1
    .parameter "view"

    .prologue
    .line 53
    iget-object v0, p0, Lcom/android/calculator2/ColorButton;->mListener:Landroid/view/View$OnClickListener;

    invoke-interface {v0, p0}, Landroid/view/View$OnClickListener;->onClick(Landroid/view/View;)V

    .line 54
    return-void
.end method

.method public onDraw(Landroid/graphics/Canvas;)V
    .locals 10
    .parameter "canvas"

    .prologue
    const-wide/16 v8, -0x1

    const/4 v2, 0x0

    .line 95
    iget-wide v3, p0, Lcom/android/calculator2/ColorButton;->mAnimStart:J

    cmp-long v0, v3, v8

    if-eqz v0, :cond_2

    .line 96
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v3

    iget-wide v5, p0, Lcom/android/calculator2/ColorButton;->mAnimStart:J

    sub-long/2addr v3, v5

    long-to-int v7, v3

    .line 98
    .local v7, animDuration:I
    const/16 v0, 0x15e

    if-lt v7, v0, :cond_1

    .line 99
    iput-wide v8, p0, Lcom/android/calculator2/ColorButton;->mAnimStart:J

    .line 108
    .end local v7           #animDuration:I
    :cond_0
    :goto_0
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getText()Ljava/lang/CharSequence;

    move-result-object v1

    .line 109
    .local v1, text:Ljava/lang/CharSequence;
    invoke-interface {v1}, Ljava/lang/CharSequence;->length()I

    move-result v3

    iget v4, p0, Lcom/android/calculator2/ColorButton;->mTextX:F

    iget v5, p0, Lcom/android/calculator2/ColorButton;->mTextY:F

    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->getPaint()Landroid/text/TextPaint;

    move-result-object v6

    move-object v0, p1

    invoke-virtual/range {v0 .. v6}, Landroid/graphics/Canvas;->drawText(Ljava/lang/CharSequence;IIFFLandroid/graphics/Paint;)V

    .line 110
    return-void

    .line 101
    .end local v1           #text:Ljava/lang/CharSequence;
    .restart local v7       #animDuration:I
    :cond_1
    invoke-direct {p0, v7, p1}, Lcom/android/calculator2/ColorButton;->drawMagicFlame(ILandroid/graphics/Canvas;)V

    .line 102
    const-wide/16 v3, 0xa

    invoke-virtual {p0, v3, v4}, Lcom/android/calculator2/ColorButton;->postInvalidateDelayed(J)V

    goto :goto_0

    .line 104
    .end local v7           #animDuration:I
    :cond_2
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->isPressed()Z

    move-result v0

    if-eqz v0, :cond_0

    .line 105
    invoke-direct {p0, v2, p1}, Lcom/android/calculator2/ColorButton;->drawMagicFlame(ILandroid/graphics/Canvas;)V

    goto :goto_0
.end method

.method public onSizeChanged(IIII)V
    .locals 0
    .parameter "w"
    .parameter "h"
    .parameter "oldW"
    .parameter "oldH"

    .prologue
    .line 71
    invoke-direct {p0}, Lcom/android/calculator2/ColorButton;->measureText()V

    .line 72
    return-void
.end method

.method protected onTextChanged(Ljava/lang/CharSequence;III)V
    .locals 0
    .parameter "text"
    .parameter "start"
    .parameter "before"
    .parameter "after"

    .prologue
    .line 82
    invoke-direct {p0}, Lcom/android/calculator2/ColorButton;->measureText()V

    .line 83
    return-void
.end method

.method public onTouchEvent(Landroid/view/MotionEvent;)Z
    .locals 2
    .parameter "event"

    .prologue
    .line 119
    invoke-super {p0, p1}, Landroid/widget/Button;->onTouchEvent(Landroid/view/MotionEvent;)Z

    move-result v0

    .line 121
    .local v0, result:Z
    invoke-virtual {p1}, Landroid/view/MotionEvent;->getAction()I

    move-result v1

    packed-switch v1, :pswitch_data_0

    .line 135
    :goto_0
    :pswitch_0
    return v0

    .line 123
    :pswitch_1
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->isPressed()Z

    move-result v1

    if-eqz v1, :cond_0

    .line 124
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->animateClickFeedback()V

    goto :goto_0

    .line 126
    :cond_0
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->invalidate()V

    goto :goto_0

    .line 131
    :pswitch_2
    invoke-virtual {p0}, Lcom/android/calculator2/ColorButton;->invalidate()V

    goto :goto_0

    .line 121
    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_2
        :pswitch_1
        :pswitch_0
        :pswitch_2
    .end packed-switch
.end method
